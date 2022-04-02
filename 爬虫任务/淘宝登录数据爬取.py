import unittest
import time 
import bs4
import unittest
import pymysql
from selenium import webdriver 
from bs4 import BeautifulSoup


class MyTestCase1(unittest.TestCase):
    @classmethod
    def setUpClass(cls)->None:
        chromed = webdriver.ChromeOptions()
        chromed.add_argument("--disable-blink-features=AutomationControlled")
        #chromed.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        cls.driver = webdriver.Chrome(options=chromed)
        cls.driver.get("https://login.taobao.com/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(6)
        # 自动登录一次
        cls.driver.find_element_by_xpath("//*[@id='fm-login-id']").send_keys("18372750282")
        cls.driver.find_element_by_xpath("//*[@id='fm-login-password']").send_keys("1999310asd")
        cls.driver.find_element_by_xpath("//*[@id='login-form']/div[4]/button").click()
        cls.driver.implicitly_wait(2)

        # 连接数据库
        cls.conn = pymysql.connect(host="localhost", port=3306,user="root",passwd="123456",db="test")
        # 创建游标对象
        cls.cursor = cls.conn.cursor()
    @classmethod
    def tearDownClass(cls)->None:
        #cls.driver.quit()
        # 关闭连接
        cls.conn.close()
        cls.cursor.close()
        pass
    
    # * 开始爬取
    def test_2(self):

        output = "D:/Pytest/爬虫任务/test.html"
        f = open(output,'w+',encoding='utf-8')

        driver = self.driver
        # 进入淘宝首页
        driver.find_element_by_xpath("//*[@id='J_SiteNavHome']/div").click()
        driver.implicitly_wait(4)

        # 请求接口，获取所有的连接、tail
        a = driver.page_source.encode('gbk','ignore').decode('gbk')
        soup = BeautifulSoup(a,"html.parser")
        #print(soup)

        # * 获取《有好货》的数据
        title_url_Data_1 = soup.find('div', 'layer clearfix').find_all('a')
        
        for i in title_url_Data_1:
            # ! 获取详情页的地址
            detail_url = i['href']
            #f.write(str(detail_url))

            # ! 获取图标地址
            img_url ="https:"+i.find('img','a-all')['src']

            # ! 获取图标标题
            title = i.find('h4').get_text()

            # ! 获取详细描述
            svolume = i.find('p').get_text()
            #插入数据库
            # 写sql，以及插入sql的参数
            sql = "insert into taobao (`img_url`,`title`,`price`,`svolume`,`evaluate`,`integral`,`detail_url`) values(%s,%s,%s,%s,%s,%s,%s)"
            param=(img_url,title,0,svolume,'NULL','NULL',detail_url)
            #param = pymysql.escape_string(param)

            # 拼接完整sql,并执行
            self.cursor.execute(sql,param)
            # 提交
            self.conn.commit()
            


if __name__ == "__main__":
    unittest.main()