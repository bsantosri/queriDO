# -*- coding: utf-8 -*-

# importing modules
import requests
import csv
from bs4 import BeautifulSoup
import pkg_resources
import unicodedata
import sys, getopt
import getHtm
import json

# variables
lnkParam    = 'http://doweb.rio.rj.gov.br/do/navegadorhtml/' \
              'mostrar.htm?id={1}&edi_id={0}'


def main(argv):

    # Default parameters
    ediParam = 0
    matParam = 0
    output = False

    try:
        opts, args = getopt.getopt(argv, "he:d:s", ["help", "edition=", "document=", "store"])
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
        elif opt in ("-s", "--store"):
            output = True
    if not opts:
        usage()
        sys.exit(2)

    return ediParam, matParam, output


def usage():
    print("usage: getMateria [--help] [--edition=<value>] [--document=<value>] [--store]")


def soupify(link):

    # http response
    response    = requests.get(link)
    rawtext     = response.content.replace('\n', ' ').replace('\r', '')
    soup        = BeautifulSoup(rawtext, 'html5lib')
    return soup


def pretty_print(soup):
    return soup.prettify()

def extract_json(materia):
    soup = soupify(materia['matLink'])
    # This becomes necessary because the raw html is too dirty (more than one head, for example)
    # and ends up confusing the parser.
    soup.head.extract()
    if soup.style is None:
        print(soup.get_text())
        sys.exit()
    else:
        soup.style.extract()
        soup.style.extract()

    enriched_output = [materia['matPathVal'], materia['matTitulo']]
    document = soup.get_text()
    output = materia['matPathVal'] + " " + materia['matTitulo'] + " " + document.encode('utf-8')
    return output

# TODO get the tokens. Right now just outputting a list of strings.
def extract_tokens(materia):
    soup = soupify(materia['matLink'])
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
    document = soup.get_text().replace(u'\u00A0', ' ')
    document = document.replace(u'\u000A', '')
    document = document.replace(u'\u0009', '')
    encoded_document = document.encode('utf-8')
    # First and last strings are "Imprimir". The penultimate line is also not needed.
    #del document[0]
    #del document[-1]
    #del document[-1]
    #del document[-1]
    #converted_docs = []
    #for token in document:
    #    converted_docs.append(token.encode('utf-8'))
    #enriched_output.extend(document)
    #return enriched_output
    matPathVal = materia['matPathVal']
    matTitulo = materia['matTitulo']
    output = matPathVal + " " + matTitulo + " " + encoded_document
    return output

def extract_html(link):
    soup = soupify(link)
    return pretty_print(soup)


if __name__ == "__main__":
    ediParam, matParam, store = main(sys.argv[1:])

    if not store:
        materias = getHtm.getedition(ediParam, False)
        for materia in materias:
            if matParam == materia['matId']:
                print(extract_tokens(materia))
                break
    else:
        extract_html(lnkParam.format(ediParam, matParam))
