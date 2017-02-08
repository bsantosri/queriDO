# From a given set of files and a dictionary of regular expressions, create
# derived documents with markdowns as given by the regexes.

from bs4 import BeautifulSoup
import re


def markdown(html, regexes):
    # - html is the HTML documents to be marked
    # - regexes is a dictionary of labels and regular expressions.
    for classname, regex in regexes.items():
        pattern = re.compile(regex)
        soup = BeautifulSoup(html, 'html5lib')
        for string in soup.strings:
            print(repr(string))
            if re.search(pattern, repr(string)):
                # class is a reserved word in Python, so we need to do some hacking here in order to enter it as a parameter.
                string.wrap(soup.new_tag('div', **{'class':classname}))
    return soup.prettify()
