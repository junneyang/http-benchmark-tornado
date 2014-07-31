#!/bin/sh

ps -ef | grep easyhttpbenchmark | grep -v grep | awk -F' '  '{ print $2 }' | xargs kill -9
ps -ef | grep easystatserver | grep -v grep | awk -F' '  '{ print $2 }' | xargs kill -9
ps -ef | grep easystatclient | grep -v grep | awk -F' '  '{ print $2 }' | xargs kill -9

