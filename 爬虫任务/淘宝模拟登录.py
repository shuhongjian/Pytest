from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver import ActionChains 
import unittest
import time     
import ddt

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # * chromed = "C:/Users/ATM/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        chromed = webdriver.ChromeOptions()
        chromed.add_argument("--disable-blink-features=AutomationControlled")
        chromed.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        cls.driver = webdriver.Chrome(options=chromed)
        cls.driver.get("https://login.taobao.com/")
        cls.driver.maximize_window()
        #* 隐式等待2s
        cls.driver.implicitly_wait(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        pass

    # ! 模拟登录
    def test_1(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='fm-login-id']").send_keys("18372750282")
        driver.find_element_by_xpath("//*[@id='fm-login-password']").send_keys("1999310asd")
        time.sleep(3)
        # * driver.find_element_by_xpath("//*[@id=‘login-form’]/div[4]/button]").click()

        # * 选中滑块
        
        try:
            print("开始获取元素-滑块")
            #driver_wait = WebDriverWait(driver, 60)
            slider = self.wait.until(EC.presence_of_element_located((
                By.ID, 'nc_1__bg'
            )))
            time.sleep(1)
            print(slider)
            print("判断元素存在:",slider.is_displayed())
            
            # ! if slider.is_displayed():
            if True:
                print("元素存在-继续执行")
                ActionChains(driver).click_and_hold(on_element=slider).perform()
                print("已选中滑块-继续执行")
                ActionChains(driver).move_by_offset(xoffset=258, yoffset=0).perform()
                print("已移动滑块-继续执行")
                ActionChains(driver).pause(0.5).release().perform()
            else:
                print("元素不存在-退出")
        except:
            print ("移动滑块失败")
        driver.find_element_by_xpath("//*[@id='login-form']/div[4]/button").click()
    

if __name__ == "__main__":
    unittest.main()