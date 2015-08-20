#!/bin/sh

rm -rf docs
epydoc --html -v -o docs mungo
