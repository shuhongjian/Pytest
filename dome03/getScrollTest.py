import time

def getScrollTest(driver: object) -> object:
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