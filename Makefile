all: clean build

.PHONY: clean build

build:
	find . -name \*.po -execdir msgfmt cantospeech.po -o cantospeech.mo \;
	./scripts/build.py
	cp ./src/templates/robots.txt ./docs
	cp -r ./src/assets/* ./docs

clean:
	rm -rf ./docs/*
