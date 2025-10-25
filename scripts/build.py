#!/usr/bin/env python3
# pylint: disable=broad-exception-caught
"""This is a simple script to include the common parts of source html files, such as header and
footer,  with the actual content"""

import os
import re
from html.parser import HTMLParser

COMPONENT_ROOT = os.path.join(os.path.dirname(__file__), '../src/components')
FILE_LIST = [
    os.path.join(os.path.dirname(__file__), '../docs/' + file) for file in
    [ 'index.html', 'about.html', 'speech_therapy.html', 'cantonese.html', 'resources.html',
      'contact.html']]

class OutOfDirectoryError(Exception):
    """This Error is raised when the source html file tries to include something outside of the
    \"components\" directory"""

    def __init__(self, msg="Stop right there criminal scum! "\
                 "You are trying to access a directory you are not supposed to!"):
        self.msg = msg
        super().__init__(msg)

    def __str__(self):
        return self.msg

class CSHTMLParser(HTMLParser):
    """CSHTMLParser or Canto Speech HTMLParse extends Python's built-in HTMLParser. It's function is
    to parse the source html files and when it encounter a processing with the correct syntax, it
    will read the correct component file and the `feed_with_return` function will return the
    required information to process the source file into a complete output file.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.component_list = []

    def handle_pi(self, data) -> None:
        target, *content = data.split(' ')

        if target == 'cs-component':
            attr, value = content[0].split('=')

            if attr == 'include':
                component = value.strip('"')
                file = os.path.join(COMPONENT_ROOT, component)
                line, offset = self.getpos()

                # Check if trying to include something outside of the component directory
                if not os.path.samefile(COMPONENT_ROOT, os.path.dirname(file)):
                    raise OutOfDirectoryError

                with open(file, 'r', encoding='utf-8') as f:
                    s = f.read()
                    self.component_list.append(
                        (line, re.sub("(^.)", ' ' * offset + r'\g<1>', s, flags=re.MULTILINE)))

    def feed_with_return(self, data) -> list:
        """Accept a source html file as input string and return the information need to process that
        file"""
        self.feed(data)
        return self.component_list

def main():
    """Pass source html files to the parse and write the output to the same source files"""
    for file in FILE_LIST:
        try:
            parser = CSHTMLParser()

            with open(file, 'r', encoding='utf-8') as f:
                data = f.read()
                component_tuples = parser.feed_with_return(data)
                data_split = data.split('\n')
                for component_tuple in component_tuples:
                    target_line, component = component_tuple
                    data_split[target_line - 1] = component.strip('\n')

            with open(file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(data_split))
        except Exception as e:
            print(f"Error processing file {file}: {e}")

if __name__ == '__main__':
    main()
