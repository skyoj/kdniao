# -*- coding: utf-8 -*-
import hashlib
import web
import receive
import reply
import kdniao
import json
import datetime

class Handle(object):
    def POST(self):
        webData = web.data()
        print type(webData)
        print "Handle Post webdata is", webData
        reqData = receive.parse_xml(webData)
        print reqData
        request_data = reqData.RequestData
        data = json.loads(request_data)
        res_data = {
            'EBusinessID': data['EBusinessID'],
            'Success': 'true',
            'UpdateTime': datetime.datetime.now().strftime("%Y-%m-%d" "%H:%M:%S")
        }
        print res_data
        return res_data