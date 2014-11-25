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
    subject = u"【测试报告】easyhttpbenchmark性能测试报告"
    content = u"<div style='color:black;text-align:center;display:block;font-size:20px;font-family:微软雅黑'>easyhttpbenchmark性能测试报告</div>"

    content += u"<div style='font-family:微软雅黑;font-size:12px;font-style:italic;text-align:center;'>"
    content += u"<a href='https://github.com/JunneYang/easyhttpbenchmark'>@easyBenchmarkTesttool</a> 2014"
    content += u"</div>"

    report = ""
    report += "======================================================================================<br/>"
    report += "|                                 TEST REPORT                                        |<br/>"
    report += "======================================================================================<br/>"
    report += "|  client_num              : XXX<br/>"
    report += "|  maxconnectoin           : XXX<br/>"
    report += "|-------------------------------------------------------------------------------------<br/>"
    report += "|  test_time(min)          : XXX<br/>"
    report += "|  total_req_cnt           : XXX<br/>"
    report += "|  total_res_cnt           : XXX<br/>"
    report += "|  total_err_cnt           : XXX<br/>"
    report += "|  total_nul_cnt           : XXX<br/>"
    report += "|  QPS(query per second)   : XXX<br/>"
    report += "|-------------------------------------------------------------------------------------<br/>"
    report += "|  avg_res_time(ms)        : XXX<br/>"
    report += "|  below_10(ms)            : XXX<br/>"
    report += "|  between_10_20(ms)       : XXX<br/>"
    report += "|  between_20_30(ms)       : XXX<br/>"
    report += "|  over_30(ms)             : XXX<br/>"
    report += "======================================================================================<br/>"
    #report = report.replace(" ","&nbsp;")
    content += report

    #img_file = u"./img/imgtest.png"
    img_file = None
    #content += u"<p><img src='cid:"+img_file+"' alt='"+img_file+"' /></p>"
    from_mail_addr = u"XXX"
    to_mail_addr = u"XXX"
    mail_server = u"XXX"

    mail_send(subject,content,img_file,from_mail_addr,to_mail_addr,mail_server)

