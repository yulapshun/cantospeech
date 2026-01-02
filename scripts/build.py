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

    def __init__(self, component_root, **kwargs) -> None:
        super().__init__(**kwargs)
        self.COMPONENT_ROOT = component_root
        self.component_tuples = []

    def handle_pi(self, data) -> None:
        target, *content = re.split(r'\s+', data.strip())

        if target == 'cs-component':
            attr, value = content[0].split('=')

            if attr == 'include':
                component = value.strip('"')
                line, offset = self.getpos()
                # length +3 to account for the 3 characters of the PI tag
                self.component_tuples.append((line - 1, offset, len(data) + 3, component))

    def render(self, data) -> str:
        """Accept the raw template file data as a string and return the final rendered HTML as a string"""
        self.feed(data)
        data_split = [list(line) for line in data.split('\n')]
        for component_tuple in reversed(self.component_tuples):
            line, offset, length, component = component_tuple
            file = os.path.join(self.COMPONENT_ROOT, component)

            # Check if trying to include something outside of the component directory
            if not os.path.samefile(self.COMPONENT_ROOT, os.path.dirname(file)):
                raise OutOfDirectoryError

            with open(file, 'r', encoding='utf-8') as f:
                s = f.read()
                print(offset)
                indented_component = '\n'.join(
                    [line if i == 0 else ' ' * offset + line
                     for i, line
                     in enumerate(s.split('\n'))])
                data_split[line][offset: offset + length] = indented_component

        return '\n'.join([''.join(line) for line in data_split])

def main():
    """Pass source html files to the parse and write the output to the same source files"""
    for file in FILE_LIST:
        try:
            parser = CSHTMLParser(COMPONENT_ROOT)
            with open(file, 'r', encoding='utf-8') as f:
                data = f.read()
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(parser.render(data))

        except Exception as e:
            print(f"Error processing file {file}: {e}")

def test_include_header_same_line():
    parser = CSHTMLParser(os.path.join(os.path.dirname(__file__), 'test/components'))
    output = parser.render("""<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Title</title>
  </head>
  <body><?cs-component include="header.html"><main>
      Main Content
    </main>
  </body>
</html>""")
    print(output)
    assert output == """<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Title</title>
  </head>
  <body><nav>
          <ul>
            <li><a href="/about.html">About <span lang="zh-Hant">關於</span></a></li>
            <li><a href="/resources.html">Resources <span lang="zh-Hant">資源</span></a></li>
            <li><a href="/contact.html">Contact <span lang="zh-Hant">聯絡我們</span></a></li>
          </ul>
        </nav>
        <main>
      Main Content
    </main>
  </body>
</html>"""


if __name__ == '__main__':
    main()
