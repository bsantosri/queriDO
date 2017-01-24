# -*- coding: utf-8 -*-

# importing modules
import requests
import csv
from bs4 import BeautifulSoup
import pkg_resources
import unicodedata
import sys, getopt

# variables
lnkParam    = 'http://doweb.rio.rj.gov.br/do/navegadorhtml/' \
              'mostrar.htm?id={0}&edi_id={1}'


def main(argv):

    # Default parameters
    ediParam = 0
    matParam = 0

    try:
        opts, args = getopt.getopt(argv, "he:d:", ["help", "edition=", "document="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-e", "--edition"):
            ediParam = arg
        elif opt in ("-d", "--document"):
            matParam = arg
    if not opts:
        usage()
        sys.exit(2)

    return ediParam, matParam


def usage():
    print("usage: getMateria [--help] [--edition=<value>] [--document=<value>]")


def soupify(edicao, materia):

    # http response
    response    = requests.get(lnkParam.format(materia, edicao))
    rawtext     = response.content.replace('\n', ' ').replace('\r', '')
    soup        = BeautifulSoup(rawtext, 'html5lib')
    return soup

# TODO get the tokens. Right now just outputting a list of strings.
def extract_tokens(soup):
    # This becomes necessary because the raw html is too dirty (more than one head, for example)
    # and ends up confusing the parser.
    soup.head.extract()
    if soup.style is None:
        print(soup.get_text())
        sys.exit()
    else:
        soup.style.extract()
        soup.style.extract()

    # This contains the text of the document separated by sentences.
    # Bear in mind that due to ugly and automated formatting when the text was originally generated
    # there might be odd splits, like one word showing up as two separate strings. This will need to
    # be taken care of when structuring the data.
    return [text for text in soup.stripped_strings]

def pretty_print(soup):
    return soup.prettify()

def extract_html(ediParam, matParam):
    soup = soupify(ediParam, matParam)
    print('Outputting html to', '../html/' + str(ediParam) + '-' + str(matParam) + '.html')
    f = open('../html/' + str(ediParam) + '-' + str(matParam) + '.html', 'w')
    htmlfile = pretty_print(soup)
    for line in htmlfile:
        f.write(line.encode('utf-8'))
    f.close()

if __name__ == "__main__":
    ediParam, matParam = main(sys.argv[1:])
    extract_html(ediParam, matParam)
