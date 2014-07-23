#!/bin/sh
processnum=$1
clientnum=$2
testtime=$3
flag=$4
testdata=$5

if [ $# != 5 ] ; then
	echo -e "Usage:\t\t./start.sh processnum clientnum testtime flag testdata"
	echo -e "Example:\t./start.sh 0 500 1 0 ./testdata/http_post_json.data"
	echo -e "more usage details please type 'python easyhttpbenchmark.py -h' for help."
	exit 1; 
fi 

python easyhttpbenchmark.py -p $processnum -c $clientnum -t $testtime -f $flag $testdata

python easystatclient.py

