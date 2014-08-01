#!/bin/sh
processnum=$1
maxclientnum=$2
clientnum=$3
testtime=$4
flag=$5
testdata=$6
from_mail_addr=$7
to_mail_addr=$8
mail_server=$9

if [ $# != 9 ] ; then
	echo -e "======================================================================================"
	echo -e "|                                 Usage Instructions                                 |"
	echo -e "======================================================================================"
	echo -e "|usage          : ./start.sh processnum maxclientnum clientnum testtime flag testdata from_mail_addr to_mail_addr mail_server"
:<<EOF
	echo -e "  processnum    : 多进程模式, 建议在高性能测试场景(QPS>1000)使用."
	echo -e "                    -1 : 关闭多进程模式;"
	echo -e "                    0  : 自动检测VCPU个数, 启动同等个数进程;"
	echo -e "                    N  : 自定义进程数, 建议N小于VCPU个数."
	echo -e "  maxclientnum  : 单进程最大连接数, 如: 1000."
	echo -e "  clientnum     : 单进程客户端个数, 如: 200"
	echo -e "  testtime      : 测试时间, 单位: 分钟, 如: 1"
	echo -e "  flag          : 是否打印控制台输出, 建议仅在调试模式下使用."
	echo -e "                    0 : 不打印;"
	echo -e "                    1 : 打印;"
	echo -e "  testdata      : 测试数据文件路径, 测试数据文件格式参考./testdata/readme.txt."
	echo -e "|-------------------------------------------------------------------------------------"
EOF
	echo -e "|example        : ./start.sh 0 1000 200 1 0 ./testdata/http_post_json.data yangjun03@baidu.com yangjun03@baidu.com mail2-in.baidu.com"
	echo -e "|-------------------------------------------------------------------------------------"
	echo -e "|more           : more usage details, type 'python easyhttpbenchmark.py -h' for help."
	echo -e "======================================================================================"
	exit 1; 
fi 

python easyhttpbenchmark.py -p $processnum -m $maxclientnum -c $clientnum -t $testtime -f $flag $testdata
#./easyhttpbenchmark -p $processnum -m $maxclientnum -c $clientnum -t $testtime -f $flag $testdata

python easystatclient.py $from_mail_addr $to_mail_addr $mail_server
#./easystatclient
