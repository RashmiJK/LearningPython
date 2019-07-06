# Paring HTML code example

from html.parser import HTMLParser

metacount = 0

class MyHTMLParser(HTMLParser):
    # overiding class methods
    # function to handle an opening tag in the doc
    # this will be called when the closing ">" of the tag is reached

    def handle_starttag(self, tag, attrs):
        global metacount
        if tag == "meta":
            metacount += 1

        print("Encountered a start tag:", tag)
        pos = self.getpos()
        print("\t At line: ", pos[0], " position ", pos[1])

        if attrs.__len__() > 0:
            print("\tAttributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])

        print("-----------")


    def handle_endtag(self, tag):
        print(" Encountered an end tag:", tag)
        pos = self.getpos()
        print("\t At line: ", pos[0], " position ", pos[1])



    def handle_data(self, data):
        if(data.isspace()):
            return
        print("Encountered some text data:", data)
        pos = self.getpos()
        print("\t At line: ", pos[0], "position", pos[1])


    def handle_comment(self, data):
        print("Encountered comment: data")
        pos = self.getpos()
        print("\t At line: ", pos[0], "position", pos[1])



def main():
    parser = MyHTMLParser()

    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()
        parser.feed(contents)


if __name__ == "__main__":
    main()