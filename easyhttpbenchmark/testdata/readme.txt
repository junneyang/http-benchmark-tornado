数据文件需使用utf-8格式：
1.protocol_type:	HTTP协议类型，仅支持POST、GET，默认post
2.data_type			HTTP请求数据类型，仅支持JSON格式，默认json
3.url_string		请求url，例："http://10.81.12.112:18080/lbs/da/openservice"
4.headers			HTTP请求头，例：{"Content-type":"application/json"}
5.body				HTTP请求body，body配置为数组形式,支持多个请求随机发送,默认只有一个请求
6.connection_tmout	连接超时时间配置，单位：ms，默认3000
7.request_tmout		请求超时时间设置，单位：ms，默认3000
