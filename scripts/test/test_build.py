import os
import pytest
from build import CSHTMLParser

@pytest.fixture
def parser():
    os.path.dirname(__file__)
    return CSHTMLParser(os.path.join(os.path.dirname(__file__), 'components'))

@pytest.mark.usefixtures('parser')
class TestHTMLParser():

    def test_empty_render(self, parser):
        output = parser.render('')
        assert output == ''

    def test_include_header(self, parser):
        output = parser.render("""<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Title</title>
  </head>
  <body>
    <?cs-component include="header.html">
    <main>
      Main Content
    </main>
  </body>
</html>""")
        assert output == """<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Title</title>
  </head>
  <body>
    <nav>
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

    def test_include_header_and_footer(self, parser):
        output = parser.render("""<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Title</title>
  </head>
  <body>
    <?cs-component include="header.html">
    <main>
      Main Content
    </main>
    <?cs-component include="footer.html">
  </body>
</html>""")
        assert output == """<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Title</title>
  </head>
  <body>
    <nav>
      <ul>
        <li><a href="/about.html">About <span lang="zh-Hant">關於</span></a></li>
        <li><a href="/resources.html">Resources <span lang="zh-Hant">資源</span></a></li>
        <li><a href="/contact.html">Contact <span lang="zh-Hant">聯絡我們</span></a></li>
      </ul>
    </nav>
    
    <main>
      Main Content
    </main>
    <footer>
      © 2199 Test. All Rights Reserved
    </footer>
    
  </body>
</html>"""

    def test_include_header_same_line(self, parser):
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
