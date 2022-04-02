import unittest
import requests
import bs4
import re
import time
import pandas
import json
from urllib.parse import urlencode
login_url = "https://bbs.yuanacg.com/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LBrIg&inajax=1"
index_url = "https://bbs.yuanacg.com/forum-39-1.html "

#登录请求，过去cookie
login_headers = {
    # "Host":"bbs.yuanacg.com",
    # "Connection":"keep-alive",
    # "Content-Length":"233",
    # "Cache-Control":"max-age=0",
    # "sec-ch-ua":"‘Chromium’;v=‘94’, ‘Google Chrome’;v=‘94’, ‘;Not A Brand’;v=‘99’",
    # "sec-ch-ua-mobile":"?0",
    # "sec-ch-ua-platform":"'Windows'",
    # "Upgrade-Insecure-Requests":"1",
    # "Origin":"https://bbs.yuanacg.com",
    "Content-Type":"application/x-www-form-urlencoded",
    # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    # "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "Sec-Fetch-Site":"same-origin",
    # "Sec-Fetch-Mode":"navigate",
    # "Sec-Fetch-User":"?1",
    # "Sec-Fetch-Dest":"iframe",
    # "Referer":"https://bbs.yuanacg.com/member.php?mod=logging&action=login&referer=https%3A%2F%2Fbbs.yuanacg.com%2Fforum.php%3Fmod%3Dforumdisplay%26fid%3D39%26page%3D1",
    # "Accept-Encoding":"gzip, deflate, br",
    # "Accept-Language":"zh-CN,zh;q=0.9",
    }
login_data = {
    #"formhash":"4f12db7a",
    "referer":"https://bbs.yuanacg.com/forum.php?mod=forumdisplay&fid=39&page=1",
    "fid":"39",
    "page":"1",
    "loginfield":"username",
    "username":"数红缰绳",
    "password":"1999310",
    "questionid":"0",
    "answer":"",
    "cookietime":"2592000"
    }
login_data = urlencode(login_data)
login_reg = requests.post(url=login_url,headers = login_headers,data=login_data)
#print(login_reg.cookies)
cookie = login_reg.headers['Set-cookie']

print(cookie)
index_headers = {
    "Cookie":cookie,
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}
login_index = requests.get(url=index_url,headers = index_headers)

print(login_index.text)