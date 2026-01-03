#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# dependencies = ["jinja2==3.1.6"]
# ///

import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), dir) for dir in ('../src/templates', '../src/templates/components'))
TEMPLATE_LIST = ('index.html', 'about.html', 'contact.html', 'resources.html', 'speech_therapy.html', 'cantonese.html')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../docs')

env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIRS),
    autoescape=select_autoescape())

for template in TEMPLATE_LIST:
    file_path = os.path.join(OUTPUT_DIR, template)
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(env.get_template(template).render())
