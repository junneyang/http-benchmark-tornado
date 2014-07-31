from xmlrpclib import ServerProxy
from common.email_lib import *
import sys

if __name__ == "__main__":
    import json
    cfg_json=json.load(open("./conf/easyhttpbenchmark.conf", "r"),encoding='utf-8')
    stat_rpc_server=cfg_json['stat_rpc_server']
    stat_rpc_port=cfg_json['stat_rpc_port']
    svr=ServerProxy("http://"+stat_rpc_server+":"+stat_rpc_port)
    print("""======================================================================================
|                                 TEST REPORT                                        |
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
        subject=cfg_json['subject']
        from_mail_addr=cfg_json['from_mail_addr']
        to_mail_addr=cfg_json['to_mail_addr']
        mail_server=cfg_json['mail_server']

        content = u"<div style='color:black;text-align:center;display:block;font-size:20px;font-family:Œ¢»Ì—≈∫⁄'>easyhttpbenchmark–‘ƒ‹≤‚ ‘±®∏Ê</div>"

        content += u"<div style='font-family:Œ¢»Ì—≈∫⁄;font-size:12px;font-style:italic;text-align:center;'>"
        content += u"<a href='https://github.com/JunneYang/easyhttpbenchmark'>@easyBenchmarkTesttool</a> 2014"
        content += u"</div>"

        report = ""
        report += "======================================================================================<br/>"
        report += "|                                 TEST REPORT                                        |<br/>"
        report += "======================================================================================<br/>"
        report += "|  client_num              : "+str(svr.ret_clientnum())+"<br/>"
        report += "|  maxconnectoin           : "+str(svr.ret_maxclientnum())+"<br/>"
        report += "|-------------------------------------------------------------------------------------<br/>"
        report += "|  test_time(min)          : "+str(svr.get_test_time())+"<br/>"
        report += "|  total_req_cnt           : "+str(svr.ret_total_req_cnt())+"<br/>"
        report += "|  total_res_cnt           : "+str(svr.ret_total_res_cnt())+"<br/>"
        report += "|  total_err_cnt           : "+str(svr.ret_total_err_cnt())+"<br/>"
        report += "|  total_nul_cnt           : "+str(svr.ret_total_nul_cnt())+"<br/>"
        report += "|  QPS(query per second)   : "+str("%0.2f" %svr.ret_qps())+"<br/>"
        report += "|-------------------------------------------------------------------------------------<br/>"
        report += "|  avg_res_time(ms)        : "+str("%0.2f" %svr.ret_avg_res_time())+"<br/>"
        report += "|  below_10(ms)            : "+str(svr.ret_total_below_10())+"<br/>"
        report += "|  between_10_20(ms)       : "+str(svr.ret_total_between_10_20())+"<br/>"
        report += "|  between_20_30(ms)       : "+str(svr.ret_total_between_20_30())+"<br/>"
        report += "|  over_30(ms)             : "+str(svr.ret_total_over_30())+"<br/>"
        report += "======================================================================================<br/>"
        #report = report.replace(" ","&nbsp;")
        content += report

        #img_file = u"./img/imgtest.png"
        img_file = None
        #content += u"<p><img src='cid:"+img_file+"' alt='"+img_file+"' /></p>"
        '''from_mail_addr = u"yangjun03@baidu.com"
        to_mail_addr = u"yangjun03@baidu.com"
        mail_server = u"mail2-in.baidu.com"'''

        mail_send(subject,content,img_file,from_mail_addr,to_mail_addr,mail_server)
    except Exception as e:
        pass

    try:
        svr.shutdown()
        svr.shutdown()
    except:
        pass
