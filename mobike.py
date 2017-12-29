#!/usr/bin/env python
# coding: utf8

import time
import requests

'''
distId = 车辆id
distX = 经度
distY = 维度
distNum = 未知
bikeIds = 车辆编号？
biketype = 车辆状态？1正常，2红包车，需测试
type = 未知
boundary = 边界？可能是停车范围，可能是行驶范围
'''

session = requests.session()
session.headers['host'] = 'mwx.mobike.com'
session.headers['content-type'] = 'application/x-www-form-urlencoded'
session.headers['opensrc'] = 'list'
session.headers['mobileno'] = ''
session.headers['wxcode'] = 'fake wxcode'
session.headers['platform'] = '3'
session.headers['accept-language'] = 'zh-cn'
session.headers['subsource'] = ''
session.headers['lang'] = 'zh'
session.headers['user-agent'] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (' \
								'KHTML, like Gecko) Mobile/15A432 MicroMessenger/6.5.19 NetType/WIFI Language/zh_CN'
session.headers['referer'] = 'https://servicewechat.com/fake/137/page-frame.html'

def main():
	session.headers['time'] = str(long(time.time() * 1000))
	session.headers['citycode'] = '010'

	body = {
	'verticalAccuracy':10,
	'speed': -1,
	'horizontalAccuracy':65,
	'accuracy':65,
	'errMsg':'getLocation:ok',
	'citycode':'010',#010=北京
	'wxcode':'fake wxcode',
	'longitude':'116.4030533',#经度
	'latitude':'39.97728',#维度
	'altitude':'46.802894592285156'#好像是海拔？
	}

	#安贞门经纬度
	#116.4030533
	#39.97728

	data = session.post(url='https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do', data=body).json()

	for bike in data['object']:
		print "{distId}\t{distX}\t{distY}\t{distance}\t{biketype}".format(**bike)

if __name__ == '__main__':
	main()
