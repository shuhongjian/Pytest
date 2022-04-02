import unittest
import requests
import pytest
import ddt
data = [
    ['liuchao'],
    ['liuchao_1'],
    ['liuchao']
]
@ddt.ddt
class TestCase_1(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @ddt.data(*data)
    @ddt.unpack
    def test_index(self,data):
        url = "http://119.36.213.90:9000/cas_server/login"
        data = {
            'service': 'http://119.36.213.90:9000/tb/bp/sys/index.html?param=eb87fead-1418-4de6-8cfb-4a0b1daf0455',
            'username': data,
            'drowssap': 'Dse@123'
        }
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
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
        response = requests.post(url, headers=headers, data=data)
        r = response.json()['result']
        url_2 = r['msg']
        seeion = requests.session()
        seeion.get(url=url_2, timeout=2)
        url_3 = "http://119.36.213.90:9000/tb/bp/sys/baseInfo/user/queryUserByToken"
        souye = requests.get(url=url_3,cookies =seeion.cookies.get_dict(),timeout=2)
        print(souye.text)
        assert '"code":200,"desc":"成功"' in souye.text


if __name__ == '__main__':
    unittest.main()
