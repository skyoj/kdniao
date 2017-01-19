# -*- coding: utf-8 -*-
import hashlib
import web
import receive
import reply
import kdniao

class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print type(webData)
            print "Handle Post webdata is", webData
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = kdniao.get_express(recMsg.Content)
                replyMsg = reply.TextMsg(toUser,fromUser,content)
                return replyMsg.send()
            else:
                print "暂不处理"
                return "success"
        except Exception, Argment:
            return Argment
