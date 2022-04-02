import selenium
from selenium import webdriver
import time

google = 'C:\\Users\\ATM\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=google)
def test_1(url_1):
    global delattr
    # 打开浏览器超时断言
    driver.implicitly_wait(30)
    # 启动浏览器并访问网站
    driver.get(url_1)
    driver.maximize_window()

    # 输入账号密码
    input_name = driver.find_element_by_id('username')
    input_name.send_keys('liuchao')
    time.sleep(3)
    input_password = driver.find_element_by_id('drowssap')
    input_password.send_keys('Dse@123')
    time.sleep(3)

#     点击登录
    link_login =driver.find_element_by_id('subBtn')
    link_login.click()

    time.sleep(3)
    try:
        #打印登录后的文本信息，并进行断言
        div_text = driver.find_element_by_class_name('el-dropdown')
        time.sleep(3)
        assert '刘超' in div_text.text

    except Exception as c:
        print("断言失败")

    driver.quit()




if __name__ == '__main__':
        test_1(url_1='http://119.36.213.90:9000/tb/bp/sys/index.html?param=eb87fead-1418-4de6-8cfb-4a0b1daf0455#/main4')
