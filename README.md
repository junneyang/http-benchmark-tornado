easyhttpbenchmark
=================

高性能http性能测试工具，web性能测试首选。解决业界web测试工具压力不足、压力不均匀、统计输出不完备、扩展不灵活等所有缺陷。    

### Feature:
* 高性能，基于异步网络框架tornado开发，单机QPS轻松达到15000左右。业界开源、业界通用测试工具要么做不到、要么需要多进程多机器联合才能达到，既需要占用紧张的机器资源、最终的性能统计也比较困难。  
* 支持随机发送。
* 统计输出完备，支持QPS统计、延迟统计。    
* 结构灵活，可方便扩展成多机结构。    

### Dependencies:    
* tornado=>>http://www.tornadoweb.org/en/stable/

### Usage:
* 运行如下命令一键式启动性能测试：    
./start.sh 0 500 1 0 ./testdata/http_post_json.data
![image](screenshot/001.jpg)     
* 命令行参数解释如下:    
![image](screenshot/002.jpg)

### Framework:    
* 测试工具架构如下：    
![image](screenshot/frame.png)     
