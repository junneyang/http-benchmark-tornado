#!/usr/bin/env python
#-*- coding: utf-8 -*-
import optparse
import os
import json

class optparse_lib(object):
    def parse_args(self):
        usage=u"""python %prog [Options] testdata
        testdata:\tpath of test data file.

        python %prog -p 0 -c 500 -t 1 -f 0 ./testdata/http_post_json.data"""
        version=u"%prog 1.0"
        parse=optparse.OptionParser(usage=usage,version=version)

        help=u'''multi-process mode,configuration number suggested to be less than the actual number of VCPU;
                -1:close multi-process mode;
                0:automatic detection of VCPU numbers and start the corresponding number of processes;
                    the default mode is 0.'''
        parse.add_option('-p','--processnum',help=help,type='int',metavar='Integer',dest="processnum",default=0)

        help=u"client number of each process"
        parse.add_option('-c','--clientnum',help=help,type='int',metavar='Integer',dest="clientnum",default=500)

        help=u"total test time,minute as unit,the default time is 2 minutes."
        parse.add_option('-t','--testtime',help=help,type='float',metavar='Float',dest="testtime",default=1)

        help=u"whether to print the std output.1 represents true,0 represents false."
        parse.add_option('-f','--flag',help=help,type='int',metavar='Integer',dest="flag",default=0)

        options,args=parse.parse_args()

        if(len(args)) != 1:
            parse.error("[ERROR]:lack datafile argument.")
            '''print(parse.format_help())
            parse.exit()'''
        if(not os.path.exists(str(args[0]))):
            parse.error("[ERROR]:data file not exist.")
        else:
            datafile_json=json.load(open(str(args[0]), "r"),encoding='utf-8')

        return options,datafile_json


if __name__ == "__main__":
    options,datafile_json=optparse_lib().parse_args()
    print(options.processnum,options.clientnum,options.testtime,options.flag,datafile_json)

