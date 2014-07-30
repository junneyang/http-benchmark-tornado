#!/usr/bin/env python
#-*- coding: utf-8 -*-
from common.optparse_lib import optparse_lib
import tornado.httpclient
import tornado.ioloop
from tornado import process
import logging
import json
import time
import os
import random

class easyhttpbenchmark(object):
    def __init__(self,maxclientnum,clientnum,testtime,flag,datafile_json):
        self.maxclientnum=maxclientnum
        self.clientnum=clientnum
        self.testtime=testtime
        self.flag=flag
        self.datafile_json=datafile_json
        self._io_loop =tornado.ioloop.IOLoop()
        self.protocol_type=self.datafile_json['protocol_type']
        self.connection_tmout=self.datafile_json['connection_tmout']
        self.request_tmout=self.datafile_json['request_tmout']
        if(self.protocol_type == 'post' or self.protocol_type == 'get'):
            self._client=tornado.httpclient.AsyncHTTPClient(self._io_loop,max_clients=self.maxclientnum)

        self.total_req_cnt=0
        self.total_res_cnt=0
        self.total_err_cnt=0
        self.total_nul_cnt=0

        self.below_10=0
        self.between_10_20=0
        self.between_20_30=0
        self.over_30=0
        self.total_res_time=0

    def benchmark_test(self):
        for i in xrange(self.clientnum):
            start_time=time.time()
            self._client.fetch(self.get_request(),  callback=lambda response:self.handle_request(response, start_time))
        self.start=time.time()
        self.end=self.start+self.testtime*60
        self._io_loop.start()
    def get_request(self):
        #could add choice to select random request in a sequence
        if(self.protocol_type == 'post'):
            url=self.datafile_json['url_string']
            headers=self.datafile_json['headers']
            body=self.datafile_json['body']
            if(len(body)==1):
                body=body[0]
            else:
                body=random.choice(body)
            body=json.JSONEncoder().encode(body)
            httprequest_post = tornado.httpclient.HTTPRequest(url=url,
            headers=headers,method="POST",body=body,connect_timeout=self.connection_tmout,request_timeout=self.request_tmout)
            #logging.info(u"Send New Request")
            self.total_req_cnt+=1
            return httprequest_post
        elif(self.protocol_type =='get'):
            url=self.datafile_json['url_string']
            httprequest_get=tornado.httpclient.HTTPRequest(url=url,
            connect_timeout=self.connection_tmout,request_timeout=self.request_tmout)
            #logging.info(u"Send New Request")
            self.total_req_cnt+=1
            return httprequest_get

    def handle_request(self,response,start_time):
        end_time=time.time()
        cost_time=(end_time-start_time)*1000
        self.total_res_time+=cost_time
        if(cost_time<10):
            self.below_10+=1
        elif(cost_time>=10 and cost_time<20):
            self.between_10_20+=1
        elif(cost_time>=20 and cost_time<30):
            self.between_20_30+=1
        else:
            self.over_30+=1

        if response.error:
            self.total_err_cnt+=1
        else:
            self.ret=response.body
            if(int(self.flag) == 1):
                print self.ret
            #logging.info(u"Recv New Response")
            if self.ret is None:
                self.total_nul_cnt+=1
            else:
                self.total_res_cnt+=1

        if time.time()>self.end:
            self._client.close()
            self._io_loop.stop()
            return

        start_time=time.time()
        self._client.fetch(self.get_request(), callback=lambda response:self.handle_request(response, start_time))

def main():
    try:
        options,datafile_json=optparse_lib().parse_args()

        #cmdstr="""nohup python easystatserver.py > /dev/null 2>&1 &"""
        cmdstr="""nohup ./easystatserver > /dev/null 2>&1 &"""
        #status,output=cmd_execute(cmdstr)
        import os
        os.system(cmdstr)

        #print(u"start benchmark test...")
        if(options.processnum != -1):
            process.fork_processes(options.processnum)
        '''logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(asctime)s) <%(message)s>',datefmt='%a,%Y-%m-%d %H:%M:%S',
            filename="./log/process."+str(tornado.process.task_id())+".log",filemode='w')'''
        logging.basicConfig(level=logging.ERROR,
                    format='[%(levelname)s] [%(asctime)s] [%(filename)s-line:%(lineno)d] [%(funcName)s-%(threadName)s] %(message)s',
                    datefmt='%a,%Y-%m-%d %H:%M:%S',
                    filename="./log/easyhttpbenchmark.log",
                    filemode='a')
        easyhttpbc=easyhttpbenchmark(options.maxclientnum,options.clientnum,options.testtime,options.flag,datafile_json)
        easyhttpbc.benchmark_test()
        #print(u"benchmark test end...")
    except Exception as e:
        logging.error(str(e))

    try:
        from xmlrpclib import ServerProxy
        cfg_json=json.load(open("./conf/easyhttpbenchmark.conf", "r"),encoding='utf-8')
        stat_rpc_server=cfg_json['stat_rpc_server']
        stat_rpc_port=cfg_json['stat_rpc_port']
        svr=ServerProxy("http://"+stat_rpc_server+":"+stat_rpc_port)
        '''print("total_req_cnt:"+str(easyhttpbc.total_req_cnt))
        print("total_res_cnt:"+str(easyhttpbc.total_res_cnt))
        print("total_err_cnt:"+str(easyhttpbc.total_err_cnt))
        print("total_nul_cnt:"+str(easyhttpbc.total_nul_cnt))'''
        import multiprocessing
        cpu_count=multiprocessing.cpu_count()
        if(options.processnum != 0):
            svr.stat_maxclientnum(options.processnum*options.maxclientnum)
            svr.stat_clientnum(options.processnum*options.clientnum)
        else:
            svr.stat_maxclientnum(cpu_count*options.maxclientnum)
            svr.stat_clientnum(cpu_count*options.clientnum)

        svr.set_test_time(easyhttpbc.testtime)
        svr.stat_total_req_cnt(easyhttpbc.total_req_cnt)
        svr.stat_total_res_cnt(easyhttpbc.total_res_cnt)
        svr.stat_total_err_cnt(easyhttpbc.total_err_cnt)
        svr.stat_total_nul_cnt(easyhttpbc.total_nul_cnt)

        svr.stat_total_below_10(easyhttpbc.below_10)
        svr.stat_total_between_10_20(easyhttpbc.between_10_20)
        svr.stat_total_between_20_30(easyhttpbc.between_20_30)
        svr.stat_total_over_30(easyhttpbc.over_30)
        svr.stat_total_res_time(easyhttpbc.total_res_time)
    except Exception as e:
        logging.error(str(e))


if __name__ == "__main__":
    main()

