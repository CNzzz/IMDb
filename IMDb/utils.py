# coding=utf-8

import requests
import json

def trans(keyword):
    data = {
    'i':keyword,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'1538802282216',
    'sign':'6e1f00ff78a3598fcee0b7632295140b',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTIME',
    'typoResult':'false',
    }
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    response = requests.post(url,data=data).text
    result = json.loads(response)
    result = result['translateResult'][0][0]['tgt']
    return result

if __name__ == '__main__':
    trans('nice to meet you')

