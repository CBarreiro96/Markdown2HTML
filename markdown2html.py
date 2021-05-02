#!/usr/bin/python3
"""
=============================== Markdown to HTML ===================================
"""
from sys import argv, stderr
import fnmatch
import os


def markdown_to_html(argv):
    # Check if you write the argument
    if len(argv) < 3 or not fnmatch.fnmatchcase(argv[1], "*.md") \
            or not fnmatch.fnmatchcase(argv[2], "*.html"):
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    try:
        # Variables
        md = {1: "h1", 2: "h2", 3: "h3", 4: "h4", 5: "h5", 6: "h6", "-": "ul", "*": "ol"}

        # check if the file exist
        with open(argv[1], "r") as file_md, open(argv[2], "w+") as file_html:
            readme = file_md.readlines()
            for i, line in enumerate(readme):
                if len(line) - len(line.lstrip("#")) > 0:
                    tag = md[len(line) - len(line.lstrip("#"))]
                    print(tag)
                    line = line.lstrip("# ")
                    line = line.rstrip("\n ")
                    file_html.write("<{}>".format(tag) + line + "</{}>\n".format(tag))
    except IOError:
        stderr.write("Missing {}\n".format(argv[1]))
    exit(1)


if __name__ == '__main__':
    markdown_to_html(argv)
