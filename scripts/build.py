#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# dependencies = ["jinja2==3.1.6"]
# ///

import os
import gettext
from os.path import isdir
from jinja2 import Environment, FileSystemLoader, select_autoescape

LOCALES_DIR = os.path.join(os.path.dirname(__file__),"../src/locales")
TEMPLATE_DIRS = [os.path.join(os.path.dirname(__file__), dir)
                 for dir in ("../src/templates", "../src/templates/components")]
TEMPLATE_LIST = ["index.html", "about.html", "contact.html", "resources.html", "speech_therapy.html", "cantonese.html"]
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../docs")
LANGUAGES = ["en", "zh"]
DEFAULT_LANGUAGE = "en"

gettext.bindtextdomain("cantospeech", LOCALES_DIR)
gettext.textdomain("cantospeech")

envs = {}
for language in LANGUAGES:
    envs[language] = Environment(
        loader=FileSystemLoader(TEMPLATE_DIRS),
        autoescape=select_autoescape(),
        extensions=["jinja2.ext.i18n"])
    translations = gettext.translation("cantospeech", localedir=LOCALES_DIR, languages=[language])
    envs[language].install_gettext_translations(translations)

for template in TEMPLATE_LIST:
    file_path = os.path.join(OUTPUT_DIR, template)
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(envs[DEFAULT_LANGUAGE].get_template(template).render())

    for language in LANGUAGES:
        if not os.path.isdir(os.path.join(OUTPUT_DIR, language)):
            os.mkdir(os.path.join(OUTPUT_DIR, language))
        file_path = os.path.join(OUTPUT_DIR, language, template)
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(envs[language].get_template(template).render())
