# From a given set of files and a dictionary of regular expressions, create
# derived documents with markdowns as given by the regexes.

from bs4 import BeautifulSoup
import re
import sys, getopt
import glob
import pickle
import os
import ast

def main(argv):

    # Default parameters
    input_location = ''
    regex_file = ''
    output_path = ''

    try:
        opts, args = getopt.getopt(argv, "hi:r:o:", ["help", "input=", "regex=", "output="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-i", "--input"):
            if arg[-1] is not '/':
                input_location = arg + '/'
            else:
                input_location = arg
        elif opt in ("-r", "--regex"):
            regex_file = arg
        elif opt in ("-o", "--output"):
            if arg[-1] is not '/':
                output_path = arg + '/'
            else:
                output_path = arg
    if not opts:
        usage()
        sys.exit(2)

    if output_path == '' or regex_file == '' or input_location == '':
        print("input, regex and output are mandatory parameters.")
        usage()
        sys.exit(2)

    return input_location, regex_file, output_path


def usage():
    print("usage: collect_htmls [--help] [--input=<path>] [--regex=<path and file>][--output=<path>]")
    print("--help: prints this usage guide and exits.")
    print("--input=<path>: pass in the path of the input htmls.")
    print("--regex=<path and file>: pass in the path and file name of the regex dictionary.")
    print("--output=<path>: pass in the path where outputs are to be stored.")




def mark_down(html, compiled_regexes):
    # - html is the HTML documents to be marked
    # - regexes is a dictionary of labels and regular expressions.
    soup = BeautifulSoup(html, 'html5lib')
    for classname, pattern in compiled_regexes.items():
        for string in soup.strings:
            #print(repr(string))
            if re.search(pattern, repr(string)):
                # class is a reserved word in Python, so we need to do some hacking here in order to enter it as a parameter.
                string.wrap(soup.new_tag('div', **{'class':classname}))
    return soup.prettify()

if __name__ == "__main__":
    input_location, regex_file, output_path = main(sys.argv[1:])
    with open(regex_file, 'r') as handle:
        regexes = ast.literal_eval(handle.read())
        compiled_regexes = {}
        for classname, regex in regexes.items():
            # pre-compile the regular expressions for efficiency
            compiled_regexes[classname] = re.compile(regex)
        for htmlfilename in glob.glob(input_location + '*.html'):
            with open(htmlfilename, 'r', encoding='utf-8') as htmlfile:
                html = htmlfile.read()
                marked_html = mark_down(html, compiled_regexes)
                filename = os.path.split(htmlfilename)[1]
                print(filename)
                with open(output_path + filename, 'wb') as f:
                    for line in marked_html:
                        f.write(line.encode('utf-8', errors='replace'))
