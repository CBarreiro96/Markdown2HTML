#!/usr/bin/python3
"""
=============================== Markdown to HTML ===================================
"""
from sys import argv, stderr
import fnmatch


def markdown_to_html(argv):

    # Check if you write the argument
    if len(argv) < 3 or not fnmatch.fnmatchcase(argv[1], "*.md") \
            or not fnmatch.fnmatchcase(argv[2], "*.html"):
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    try:
        # Variables
        md = {1: "h1", 2: "h2", 3: "h3", 4: "h4", 5: "h5", 6: "h6", "-": "ul", "*": "ol"}
        Identifier = 0

        # check if the file exist read and write file.
        with open(argv[2], "w+") as file_html, open(argv[1], "r") as file_md:
            readme = file_md.readlines()
            for i, line in enumerate(readme):

                # Change '#' with heading tag
                if len(line) - len(line.lstrip("#")) > 0:
                    tag = md[len(line) - len(line.lstrip("#"))]
                    # String without '#'
                    line = line.lstrip("# ")
                    # String without '\n'
                    line = line.rstrip("\n ")
                    file_html.write("<{}>".format(tag) + line + "</{}>\n".format(tag))

                #  Unordered and Ordered listing
                elif len(line)-len(line.lstrip('-*')) > 0:
                    # tag <ul>
                    tag = md[line[0]]
                    # String without '*- '
                    String_li = line.lstrip("*- ")
                    # String without '\n'
                    String_li = String_li.rstrip("\n ")

                    # write in html file tag <ul> or <ol> Start
                    if Identifier != 1:
                        file_html.write("<{}>\n".format(tag))
                        Identifier = 1

                    # write in html file tag <li> Start and final
                    file_html.write("<li>" + String_li + "</li>" + "\n")

                    # write in html file final tag </ul> or <ol>
                    if i == len(readme) - 1 or readme[i + 1][0] != line[0]:
                        file_html.write("</{}>\n".format(tag))
                        Identifier = 0

    except IOError:
        stderr.write("Missing {}\n".format(argv[1]))
    exit(1)


if __name__ == '__main__':
    markdown_to_html(argv)
