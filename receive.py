# -*- coding: utf-8 -*-
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    return TextMsg(xmlData)
class Msg(object):
    def __init__(self, xmlData):
        self.RequestType = xmlData.find('RequestType').text
        self.DataSign = xmlData.find('DataSign').text
class TextMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.RequestData = xmlData.find('RequestData')