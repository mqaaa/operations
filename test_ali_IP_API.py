#_*_ coding: UTF-8 _*_
import urllib, sys
import urllib.request

host = 'http://iploc.market.alicloudapi.com'
path = '/v3/ip'
method = 'GET'
appcode = '5fde0084e5df4d5da8a2efb86a65cb8a'
querys = 'ip='+sys.argv[1]
bodys = {}
url = host + path + '?' + querys

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib.request.urlopen(request)
content = response.read()
if (content):
	print(content.decode('utf8'))
