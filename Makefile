all: clean build

.PHONY: clean build

build:
	cp -r ./src/assets/* ./docs
	./scripts/build.py

clean:
	rm -rf ./docs/*
