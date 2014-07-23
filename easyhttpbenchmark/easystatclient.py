from xmlrpclib import ServerProxy

if __name__ == "__main__":
    svr=ServerProxy("http://localhost:4321")
    print("********************test report********************")
    print("test_time:"+str(svr.get_test_time())+" min")
    print("total_req_cnt:"+str(svr.ret_total_req_cnt()))
    print("total_res_cnt:"+str(svr.ret_total_res_cnt()))
    print("total_err_cnt:"+str(svr.ret_total_err_cnt()))
    print("total_nul_cnt:"+str(svr.ret_total_nul_cnt()))
    print("QPS(query per second):"+str(svr.ret_qps()))
    print("\n")

    print("avg_res_time(ms):"+str(svr.ret_avg_res_time()))
    print("below_10(ms):"+str(svr.ret_total_below_10()))
    print("between_10_20(ms):"+str(svr.ret_total_between_10_20()))
    print("between_20_30(ms):"+str(svr.ret_total_between_20_30()))
    print("over_30(ms):"+str(svr.ret_total_over_30()))
    print("***************************************************")

    try:
        svr.shutdown()
        svr.shutdown()
    except:
        pass
