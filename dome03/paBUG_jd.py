import selenium
import xlwt
import time
import bs4
import re
import sys
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from getScrollTest import getScrollTest


opt = Options()
opt.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
opt.add_argument('window-size=1920x3000')  # 设置浏览器分辨率
opt.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
opt.add_argument('--hide-scrollbars')  # 隐藏滚动条，应对一些特殊页面
opt.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片，提升运行速度
opt.add_argument('--headless')  # 浏览器不提供可视化界面。Linux下如果系统不支持可视化不加这条会启动失败
# driver = Chrome(options=opt) 　　　　# 创建无界面对象

chromed = "C:\\Users\\ATM\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"  # 手动指定使用的浏览器位置+

driver = webdriver.Chrome(executable_path=chromed)
driver.maximize_window()

value_name = []
value_price = []
# 进入京东


def index(self):
    try:
        driver.get(self)
        time.sleep(3)
        print("访问成功")
    except:
        print("访问京东失败")

# 输入关键字


def search(self):
    try:
        driver.find_element_by_xpath(
            "//*[@id='search']/div/div[2]/input").send_keys(self)
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='search']/div/div[2]/button").click()
        print("打印所有窗口的句柄", driver.window_handles)
        print("查询成功")
    except:
        print("输入关键字失败，没有抓取到元素")


# 滚动到最低部
"""
def getScrollTest():
    js = "window.scrollTo(100, 100)"
    driver.execute_script(js)
    print("开始滚动")
    try:
        for i  in  range(15):
            time.sleep(1)
            driver.execute_script( "window.scrollTo(100, %s)"%(250 + 800*i))
        print("已滚动到最低部")
    except:
        print("已滚动到最低部")
"""
# 开始爬数据
sys.path.append('paqu')
def paqu():
    nums = 1
    for j in range(1,20):
        
        getScrollTest(driver)
        print("开始抓取第{0}页的数据".format(nums))
        a = driver.page_source.encode("gbk", "ignore").decode("gbk")
        soup = BeautifulSoup(a, "html.parser")
        """
        print("将源码写进txt")
        f = open("D:\\Pytest\\dome03\\输入与输出\\源码.txt", 'w', encoding='utf-8')
        f.write(str(soup))
        print("已写进")
        """
        title_url_Data = soup.find('div', 'goods-list-v2 gl-type-1 J-goods-list').find_all('li')
        
        for i in title_url_Data:
            pa_name = i.find('div', 'p-name p-name-type-2').find('em')
            pa_price = i.find('div', 'p-price').find('i')
            """
            print("商品名称：",pa_name.text)
            print("商品价格：",pa_price.text)
            """
            name = str(pa_name.text)
            pric = str(pa_price.text)
            value_name.append(name)
            value_price.append(pric)
        nums = nums+1

        driver.find_element_by_class_name("fp-next").click()

# 开始将爬取的数据输出到表
def shuchu():
    index_len = len(value_name)
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("sheetname")
    for i in range(index_len):
        sheet.write(i, 0, value_name[i])
        sheet.write(i, 1, value_price[i])
    workbook.save("D:\\Pytest\\dome03\\输入与输出\\结果.xls")
    print("爬取结束，已输出到表格")


if __name__ == '__main__':
    index("https://www.jd.com")
    search("RTX3060")
    paqu()
    shuchu()
