import requests

url = "http://119.36.213.90:9000/cas_server/noflow1"

data = {
    'service':'http://119.36.213.90:9000/tb/bp/sys/index.html?param=eb87fead-1418-4de6-8cfb-4a0b1daf0455',
    'username':'liuchao',
    'drowssap':'Dse@123'
}
headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '153',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'JSESSIONID=639DEDAA1D4BCA1E8627E3A27D9FF6E2',
    'Host': '119.36.213.90:9000',
    'Origin': 'http://119.36.213.90:9000',
    'Pragma': 'no-cache',
    'Referer': 'http://119.36.213.90:9000/cas_server/login?service=http%3A%2F%2F119.36.213.90%3A9000%2Ftb%2Fbp%2Fsys%2Findex.html%3Fparam%3Deb87fead-1418-4de6-8cfb-4a0b1daf0455',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

response = requests.post(url,headers=headers,data=data)


r = response.json()['result']
print(r)
# 请求下一个重定向的url
url_1=r['msg']
print(url_1)
data_1 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID=0F91920AB7546AEAA43C464054A38EF1',
    'Host': '119.36.213.90:9000',
    'Origin': 'http://119.36.213.90:9000',
    'Pragma': 'no-cache',
    'Referer': 'http://119.36.213.90:9000/cas_server/login?service=http%3A%2F%2F119.36.213.90%3A9000%2Ftb%2Fbp%2Fsys%2Findex%2Findex%3FrandomPar%3D0.35859182878981455',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Upgrade-Insecure-Requests': '1'
}
t = requests.Session()
# t = requests.get(url=url_1,timeout=2)
urrl = requests.get(url = url_1,timeout=2)
t.get(url=url_1,timeout=2)



a = t.cookies
print(a.get_dict())



# print(r.headers)


