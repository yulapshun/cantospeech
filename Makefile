all: clean build

.PHONY: build
build:
	cp -r ./src/* ./build

.PHONY: clean
clean:
	rm -rf ./build/*
