#!/usr/bin/env python
#-*- coding: utf-8 -*-

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

import sys
import os
sys.path.append("%s/../"%os.path.dirname(os.path.realpath(__file__)))

def mail_send(subject,content,img_file,from_mail_addr,to_mail_addr,mail_server):
    mail = MIMEMultipart()
    mail["Subject"] = subject
    if(img_file):
        fp=open(img_file)
        img=MIMEImage(fp.read())
        fp.close()
        img.add_header('Content-ID','<'+img_file+'>')
        mail.attach(img)
    content = MIMEText(content,'html','utf-8')
    mail.attach(content)

    mail["From"]=from_mail_addr
    mail["To"]=to_mail_addr
    smtp=smtplib.SMTP(mail_server)
    smtp.sendmail(mail["From"], mail["To"].split(","), mail.as_string())
    smtp.quit()

if __name__ == '__main__':
    subject = u"easyhttpbenchmark性能测试报告"
    content = u"<h1 style='color:black;text-align:center;font-size:20px;font-family:微软雅黑'>easyhttpbenchmark性能测试报告</h1>"

    content += u"<p style='font-family:微软雅黑;font-size:12px;font-style:italic;text-align:right;margin-right:50%'>"
    content += u"<a href='https://github.com/JunneYang/easyhttpbenchmark'>@easyBenchmarkTesttool</a> 2014"
    content += u"</p>"

    report = ""
    report += "<p>======================================================================================</p>"
    report += "<p>|                                 TEST REPORT                                        |</p>"
    report += "<p>======================================================================================</p>"
    report += "<p>|  client_num              : XXX</p>"
    report += "<p>|  maxconnectoin           : XXX</p>"
    report += "<p>|-------------------------------------------------------------------------------------</p>"
    report += "<p>|  test_time(min)          : XXX</p>"
    report += "<p>|  total_req_cnt           : XXX</p>"
    report += "<p>|  total_res_cnt           : XXX</p>"
    report += "<p>|  total_err_cnt           : XXX</p>"
    report += "<p>|  total_nul_cnt           : XXX</p>"
    report += "<p>|  QPS(query per second)   : XXX</p>"
    report += "<p>|-------------------------------------------------------------------------------------</p>"
    report += "<p>|  avg_res_time(ms)        : XXX</p>"
    report += "<p>|  below_10(ms)            : XXX</p>"
    report += "<p>|  between_10_20(ms)       : XXX</p>"
    report += "<p>|  between_20_30(ms)       : XXX</p>"
    report += "<p>|  over_30(ms)             : XXX</p>"
    report += "<p>======================================================================================</p>"
    report = report.replace(" ","&nbsp;")
    content += report

    #img_file = u"./img/imgtest.png"
    img_file = None
    #content += u"<p><img src='cid:"+img_file+"' alt='"+img_file+"' /></p>"
    from_mail_addr = u"yangjun03@baidu.com"
    to_mail_addr = u"yangjun03@baidu.com"
    mail_server = u"mail2-in.baidu.com"

    mail_send(subject,content,img_file,from_mail_addr,to_mail_addr,mail_server)



