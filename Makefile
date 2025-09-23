all: clean build

.PHONY: build
build:
	cp -r ./src/* ./docs

.PHONY: clean
clean:
	rm -rf ./build/*
