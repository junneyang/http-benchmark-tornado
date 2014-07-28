#helloserver.py
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SocketServer import ThreadingMixIn

class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):pass

finished=False
total_req_cnt=0
total_res_cnt=0
total_err_cnt=0
total_nul_cnt=0

test_time=0

total_below_10=0
total_between_10_20=0
total_between_20_30=0
total_over_30=0
total_res_time=0

maxclientnum=0

def stat_total_req_cnt(req_cnt):
    global total_req_cnt
    total_req_cnt+=req_cnt
def ret_total_req_cnt():
    global total_req_cnt
    return total_req_cnt

def stat_total_res_cnt(res_cnt):
    global total_res_cnt
    total_res_cnt+=res_cnt
def ret_total_res_cnt():
    global total_res_cnt
    return total_res_cnt

def stat_total_err_cnt(err_cnt):
    global total_err_cnt
    total_err_cnt+=err_cnt
def ret_total_err_cnt():
    global total_err_cnt
    return total_err_cnt

def stat_total_nul_cnt(nul_cnt):
    global total_nul_cnt
    total_nul_cnt+=nul_cnt
def ret_total_nul_cnt():
    global total_nul_cnt
    return total_nul_cnt

def set_test_time(testtime):
    global test_time
    test_time=testtime
def get_test_time():
    global test_time
    return test_time

def ret_qps():
    global total_res_cnt
    global test_time
    return total_res_cnt/(test_time*60)

def stat_total_below_10(below_10):
    global total_below_10
    total_below_10+=below_10
def ret_total_below_10():
    global total_below_10
    return total_below_10

def stat_total_between_10_20(between_10_20):
    global total_between_10_20
    total_between_10_20+=between_10_20
def ret_total_between_10_20():
    global total_between_10_20
    return total_between_10_20

def stat_total_between_20_30(between_20_30):
    global total_between_20_30
    total_between_20_30+=between_20_30
def ret_total_between_20_30():
    global total_between_20_30
    return total_between_20_30

def stat_total_over_30(over_30):
    global total_over_30
    total_over_30+=over_30
def ret_total_over_30():
    global total_over_30
    return total_over_30

def stat_total_res_time(res_time):
    global total_res_time
    total_res_time+=res_time
def ret_total_res_time():
    global total_res_time
    return total_res_time
def ret_avg_res_time():
    global total_res_time
    global total_res_cnt
    return total_res_time/total_res_cnt

def stat_maxclientnum(max_clientnum):
    global maxclientnum
    maxclientnum=max_clientnum
def ret_maxclientnum():
    global maxclientnum
    return maxclientnum

def shutdown():
    global finished
    finished = True
    return 1

def stat():
    import json
    cfg_json=json.load(open("./conf/easyhttpbenchmark.conf", "r"),encoding='utf-8')
    stat_rpc_server=cfg_json['stat_rpc_server']
    stat_rpc_port=cfg_json['stat_rpc_port']
    svr=SimpleXMLRPCServer((stat_rpc_server, int(stat_rpc_port)), allow_none=True)
    #svr=ThreadXMLRPCServer(("", 4321), allow_none=True)
    print 'started...'
    svr.register_function(stat_total_req_cnt)
    svr.register_function(ret_total_req_cnt)
    svr.register_function(stat_total_res_cnt)
    svr.register_function(ret_total_res_cnt)
    svr.register_function(stat_total_err_cnt)
    svr.register_function(ret_total_err_cnt)
    svr.register_function(stat_total_nul_cnt)
    svr.register_function(ret_total_nul_cnt)
    svr.register_function(shutdown)
    svr.register_function(set_test_time)
    svr.register_function(get_test_time)
    svr.register_function(ret_qps)

    svr.register_function(stat_total_below_10)
    svr.register_function(ret_total_below_10)
    svr.register_function(stat_total_between_10_20)
    svr.register_function(ret_total_between_10_20)
    svr.register_function(stat_total_between_20_30)
    svr.register_function(ret_total_between_20_30)
    svr.register_function(stat_total_over_30)
    svr.register_function(ret_total_over_30)
    svr.register_function(stat_total_res_time)
    svr.register_function(ret_total_res_time)
    svr.register_function(ret_avg_res_time)

    svr.register_function(stat_maxclientnum)
    svr.register_function(ret_maxclientnum)

    while not finished:
        #svr.serve_forever()
        svr.handle_request()
    print 'exited...'

if __name__ == "__main__":
    stat()

