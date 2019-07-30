'''
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(),"html.parser")

elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(elems)
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

pElems = exampleSoup.select('p')
print('-------')
print(len(pElems))
print(pElems)
print('-------')
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())
'''
'''
soup = bs4.BeautifulSoup(open('example.html'),"html.parser")
spanElem = soup.select('span')[0]
print(str(spanElem))
print(type(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)
'''
import webbrowser
import requests
import sys
import logging
import pyperclip
logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__" :    
    if len(sys.argv) > 1 :
        # Get the address from the command line
        logging.debug(len(sys.argv))
        logging.debug(sys.argv)
        search_string = ' '.join(sys.argv[1:])                
    else:
        # Get the address from clipboard
        search_string = pyperclip.paste()
       
    #webbrowser.open('https://www.google.com/search?&q=' + search_string)
    #webbrowser.open('https://www.youtube.com/results?search_query=' + search_string)
    session = requests.Session()
    session.proxies = {"https": "https://proxy-png.intel.com:912"}
    #response = session.get('https://www.google.com/search?&q=' + search_string)
    response = session.get('https://www.youtube.com/results?search_query=' + search_string)
    logging.debug(response.url)
    try:
        response.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
        exit()
    
    
    
