下载即可使用，无需安装。
1、运行 ./start_build.sh -h 查看使用方法：
======================================================================================
|                                 Usage Instructions                                 |
======================================================================================
|usage          : ./start_build.sh processnum maxclientnum clientnum testtime flag testdata
|example        : ./start_build.sh 0 1000 200 1 0 ./testdata/http_post_json.data
|-------------------------------------------------------------------------------------
|more           : more usage details, type './easyhttpbenchmark -h' for help.
======================================================================================

2、各参数详细解释如下：
processnum      : 进程数, 测试工具支持多进程, 建议在高性能测试场景下(QPS>1000)开启;
                    -1 : 关闭多进程模式, 启动一个进程;
                    0  : 多进程模式, 进程数为VCPU个数;
                    N  : 多进程模式, 进程数为N, 建议N小于VCPU个数.
maxclientnum    : 单个进程允许最大连接数, 如: 1000.
clientnum       : 单个进程客户端个数, 如: 200.
testtime        : 测试时间, 单位: min, 如: 1.
flag            : 是否在控制台打印请求相应, 0: 不打印; 1: 打印输出, 建议仅在调试模式下使用.
testdata        : 测试数据文件, 格式要求与详细配置参考 ./testdata/readme.txt .

