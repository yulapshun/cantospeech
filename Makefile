all: test clean build

.PHONY: test clean build

test:
	pytest

build:
	cp -r ./src/* ./docs
	./scripts/build.py

clean:
	rm -rf ./docs/*
