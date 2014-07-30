#!/bin/sh
pyinstaller -F easystatserver.py
pyinstaller -F easystatclient.py
pyinstaller -F easyhttpbenchmark_build.py
cp ./dist/* .
rm -rf build dist *.spec
mv easyhttpbenchmark_build easyhttpbenchmark

