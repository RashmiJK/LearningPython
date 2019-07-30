import sys
import getopt
import io
import re
from functools import reduce

# List storing long file contents line wise
fileContent = []
responsesDetails = []
zerothPktTime = 0
lastPktTime = 0
missingSeqList = []
hdrChecksumMisList = []
plChecksumMisList = []
plStatusFailureList = []
plFooterSyncByteFailureList = []
myStruct = {'seq_no':0,'arrival_time':0,'header_checksum': False, 'payload_checksum':False,'response_data':[]}

def get_sec(time_str):
    """
    :param time_str:
    :return:
    """
    h,m,sec = time_str.split(':')
    s,ms = sec.split('.')
    return (int(h)*3600000) + (int(m)*60000) + (int(s) * 1000) + int(ms)


def get_checksum(bytes_list,length):
    """
    :param bytes_list: input list
    :param length: how many checksum bytes
    :return: checksum value
    """
    # if length == 2:
    #     print(" get_checksum = ",bytes_list)
    if length == 1 :
        return reduce(lambda x,y : x + y,bytes_list,0) % 256
    elif length == 2  :
        return reduce(lambda x, y: x + y, bytes_list,0) % 65536
    else :
        return 0

def stat_v_class():
    """
    :return:
    Grepping for "zxVd" command and if found further grepping for "zxVD" response.
    """
    # "chip send data to host" command : zxVdP = Command to CP CPU, zxVdM = Command to ME CPU
    commands = ["zxVdP", "zxVdM"]
    responses = ["zxVDP", "zxVDM"]

    if len(fileContent):
        for lineIndex, lineContent in enumerate(fileContent):
            if any(cmd in lineContent for cmd in commands):
                line_content_list = fileContent[lineIndex + 2].split()  # 2 lines further is the command in hex format
                print("[", lineIndex+2, "]", fileContent[lineIndex + 2])
                which_cpu = int(line_content_list[9],base=16)
                if which_cpu == 80 or which_cpu == 77:  # 'P' or 'M'
                    if which_cpu == 80:
                        print("CP CPU :", end="")
                    elif which_cpu == 77:
                        print("ME CPU :", end="")
                    if line_content_list[13] == "C9":  # Is it 100 packet test
                        print(" 100 packets test", " with period = ", int(line_content_list[14], base=16), end="")
                        print(" and packet size as =", int(''.join(line_content_list[16:14:-1]), base=16))
                        # Response for both CPUs are same format and is found only after the command log in the file
                        response_index = lineIndex + 2 + 1
                        responses_total = 0
                        expected_seq_no = 0
                        global missingSeqList
                        global hdrChecksumMisList
                        global plChecksumMisList
                        global zerothPktTime
                        global lastPktTime
                        # logic to extract response bytes
                        while response_index < len(fileContent): # until the end of log file
                            #  print("response_index = ",response_index)
                            # finding "zxVDP" or "zxVDM" place
                            if any(res in fileContent[response_index] for res in responses):
                                # for each of response packet found perform this action
                                response_pkt_index = response_index + 1  # finding the response packet bytes
                                response_pkt_list=[]
                                response_pkt_header_checksum = False
                                response_pkt_payload_checksum = False
                                response_pkt_arrv_time = ''
                                response_pkt_bytes = []
                                response_pkt_seq_no = 0
                                flag_found_response_pkt = False
                                response_pkt_bytes = []
                                response_pkt_seq_no = 0
                                while response_pkt_index < len(fileContent):
                                    if "Response" in fileContent[response_pkt_index]:
                                        break
                                    if "Event:" in fileContent[response_pkt_index]:
                                        flag_found_response_pkt = True
                                        temp_str =  fileContent[response_pkt_index].strip('\n')
                                        if len(temp_str):
                                            response_pkt_arrv_time = temp_str.split()[1]
                                            response_pkt_list.append(" ".join(temp_str.split()[3:]))
                                    elif flag_found_response_pkt:
                                        temp_str = fileContent[response_pkt_index].strip("\n<")
                                        if len(temp_str):
                                            response_pkt_list.append(temp_str)
                                    response_pkt_index += 1
                                # print("response_pkt_list = ",response_pkt_list)
                                for item in response_pkt_list:
                                    for eachByte in item.split():
                                        response_pkt_bytes.append(int(eachByte,base=16))
                                print("---------------------")
                                print("Arrival time : ",response_pkt_arrv_time," Size : ",len(response_pkt_bytes) , end ="") # ,"->", response_pkt_bytes)
                                response_index = response_pkt_index

                                response_pkt_seq_no = (response_pkt_bytes[11]<<8)|(response_pkt_bytes[10])
                                print(" Seq No : ",response_pkt_seq_no)

                                #  extract header bytes
                                if get_checksum(response_pkt_bytes[2:7],1) == response_pkt_bytes[7] :
                                    response_pkt_header_checksum =  True
                                if response_pkt_header_checksum == False:
                                    hdrChecksumMisList.append(response_pkt_seq_no)

                                # extract payload bytes
                                payload_len = ((response_pkt_bytes[6] << 8) | response_pkt_bytes[5] )
                                # print("payload_len = ",payload_len)

                                # XMM7560_Introduction_A0.doc for byte positions
                                payload_checksum = ((response_pkt_bytes[payload_len + 7] << 8) | response_pkt_bytes[payload_len + 6] )
                                # print("payload_checksum in the packet = ",payload_checksum)
                                payload_checksum_computed = get_checksum(response_pkt_bytes[8:(payload_len+6)],2)
                                # print("Computed : payload_checksum_computed = ",payload_checksum_computed)
                                if payload_checksum_computed == payload_checksum :
                                    response_pkt_payload_checksum = True
                                if response_pkt_payload_checksum == False :
                                    plChecksumMisList.append(response_pkt_seq_no)

                                # Status byte
                                if response_pkt_bytes[8] != 32:
                                    plStatusFailureList.append(response_pkt_seq_no)

                                # Footer Sync byte
                                if response_pkt_bytes[payload_len + 8] != 10:
                                    plFooterSyncByteFailureList.append(response_pkt_seq_no)

                                if response_pkt_seq_no == 0:
                                    zerothPktTime = get_sec(response_pkt_arrv_time)

                                lastPktTime = get_sec(response_pkt_arrv_time)  #  it can be 100th or something else

                                if response_pkt_seq_no > expected_seq_no :
                                    for i in range (expected_seq_no,response_pkt_seq_no) :
                                        missingSeqList.append(expected_seq_no)
                                        expected_seq_no += 1

                                expected_seq_no += 1
                                responses_total += 1

                                myStruct['seq_no'] = response_pkt_seq_no
                                myStruct['arrival_time'] = response_pkt_arrv_time
                                myStruct['header_checksum'] = response_pkt_header_checksum
                                myStruct['payload_checksum'] = response_pkt_payload_checksum
                                myStruct['response_data'] = response_pkt_bytes[13:(payload_len+5)]
                                responsesDetails.append(myStruct)

                            elif "zxVd" in fileContent[response_index]:
                                break  # break from outer while as another command found
                            response_index += 1

                        # for those cases where trailing sequence numbers are missing and the total logs less than 100
                        while expected_seq_no < 100 :
                            missingSeqList.append(expected_seq_no)
                            expected_seq_no += 1

                        print("Total logs received = ", responses_total, "Time interval in mS = ",lastPktTime,"-",zerothPktTime,"=",
                              (lastPktTime - zerothPktTime))
                        if responses_total < 100:
                            print("Missing sequence numbers : ", len(missingSeqList) ," : ",missingSeqList)
                        if len(hdrChecksumMisList) :
                            print("Sequences with header checksum mismatch : ", hdrChecksumMisList)
                        if len(plChecksumMisList):
                            print("Sequences with payload checksum mismatch : ", plChecksumMisList)
                        if len(plStatusFailureList):
                            print("Sequences with Status byte failure : ", plStatusFailureList)
                        if len(plFooterSyncByteFailureList):
                            print("Sequences with Footer Sync Byte failure : ", plFooterSyncByteFailureList)
                        print("-----------------------")

                        break  # from outermost for loop as full file is traversed

    else:
        print("File is empty")
        sys.exit(2)


def read_log_file(logfile,outfile):
    global fileContent
    infile = open(logfile,"r")    
    fileContent = infile.readlines()    
    infile.close()
    

def main(argv):
    outfile = ""
    logfile = ""
    try:
        opts,args = getopt.getopt(argv,"hi:o:")
    except getopt.GetoptError:
        print("%s -i <inputfile>" % argv[0])
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("%s -i <inputfile>"% argv[0])
        elif opt == "-i":
            logfile = arg
        elif opt == "-o" :
            outfile = arg      
    if outfile != "":
        print("Results written to %s" % outfile)
    if logfile != "":
        print("\nParsing log file %s\n" % logfile)
        read_log_file(logfile,outfile)
        # stat_vclass()
        stat_v_class()
    else:
        print("-i <inputfile>")
                  
if __name__ == "__main__":
    # script name is at 0th index and need 2 more arguments
    if len(sys.argv) < 3:
        print("test.py -i <inputfile>")
    else:
        main(sys.argv[1:])


