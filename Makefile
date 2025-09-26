all: clean build

.PHONY: build
build:
	cp -r ./src/* ./docs
	./scripts/build.py

.PHONY: clean
clean:
	rm -rf ./docs/*
