all: clean build

.PHONY: clean build

build:
	find . -name \*.po -execdir msgfmt cantospeech.po -o cantospeech.mo \;
	./scripts/build.py
	cp -r ./src/assets/* ./docs

clean:
	rm -rf ./docs/*
