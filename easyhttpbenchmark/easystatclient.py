from xmlrpclib import ServerProxy

if __name__ == "__main__":
    import json
    cfg_json=json.load(open("./conf/easyhttpbenchmark.conf", "r"),encoding='utf-8')
    stat_rpc_server=cfg_json['stat_rpc_server']
    stat_rpc_port=cfg_json['stat_rpc_port']
    svr=ServerProxy("http://"+stat_rpc_server+":"+stat_rpc_port)
    print("""======================================================================================
|                                 TEST REPORT                                 |
======================================================================================""")
    print("""|  client_num              : """+str(svr.ret_clientnum()))
    print("""|  maxconnectoin           : """+str(svr.ret_maxclientnum()))
    print("""|-------------------------------------------------------------------------------------""")

    print("""|  test_time(min)          : """+str(svr.get_test_time()))
    print("""|  total_req_cnt           : """+str(svr.ret_total_req_cnt()))
    print("""|  total_res_cnt           : """+str(svr.ret_total_res_cnt()))
    print("""|  total_err_cnt           : """+str(svr.ret_total_err_cnt()))
    print("""|  total_nul_cnt           : """+str(svr.ret_total_nul_cnt()))
    print("""|  QPS(query per second)   : """+str("%0.2f" %svr.ret_qps()))
    print("""|-------------------------------------------------------------------------------------""")

    print("""|  avg_res_time(ms)        : """+str("%0.2f" %svr.ret_avg_res_time()))
    print("""|  below_10(ms)            : """+str(svr.ret_total_below_10()))
    print("""|  between_10_20(ms)       : """+str(svr.ret_total_between_10_20()))
    print("""|  between_20_30(ms)       : """+str(svr.ret_total_between_20_30()))
    print("""|  over_30(ms)             : """+str(svr.ret_total_over_30()))
    print("""======================================================================================""")

    try:
        svr.shutdown()
        svr.shutdown()
    except:
        pass
