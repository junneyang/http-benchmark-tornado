#!/bin/sh

ps -ef | grep easyhttpbenchmark.py | grep -v grep | awk -F' '  '{ print $2 }' | xargs kill -9
ps -ef | grep easystatserver.py | grep -v grep | awk -F' '  '{ print $2 }' | xargs kill -9
ps -ef | grep easystatclient.py | grep -v grep | awk -F' '  '{ print $2 }' | xargs kill -9

