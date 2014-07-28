#!/bin/sh
processnum=$1
maxclientnum=$2
clientnum=$3
testtime=$4
flag=$5
testdata=$6

if [ $# != 6 ] ; then
	echo -e "======================================================================================"
	echo -e "|                                 Usage Instructions                                 |"
	echo -e "======================================================================================"
	echo -e "|usage		: ./start.sh processnum maxclientnum clientnum testtime flag testdata"
	echo -e "|example	: ./start.sh 0 1000 200 1 0 ./testdata/http_post_json.data"
	echo -e "|-------------------------------------------------------------------------------------"
	echo -e "|more usage details please type 'python easyhttpbenchmark.py -h' for help."
	echo -e "======================================================================================"
	exit 1; 
fi 

python easyhttpbenchmark.py -p $processnum -m $maxclientnum -c $clientnum -t $testtime -f $flag $testdata

python easystatclient.py

