#! C:\Windows\py.exe
"""Retrieve and print words from a URL.

Usage:
    python3 words.py <URL>
"""
print('rashmi')
import urllib.request
import sys

proxy = urllib.request.ProxyHandler({'http':'proxy-png.intel.com:911'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)


#'http://sixty-north.com/c/t.txt'
def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from
        the document.
    """
    with urllib.request.urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line.

    Args:
        An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL.

    Args:
        url: The URL of a UTF-8
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__' :
    main(sys.argv[1]) # The 0th arg is the module filename