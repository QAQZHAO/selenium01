from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()

    def test_prop(self):
        print(self.driver.name)#浏览器名称
        print(self.driver.current_url)#url
        print(self.driver.title)#标题
        print(self.driver.window_handles)#句柄
        print(self.driver.page_source)#源码

        self.driver.quit()

    def test_method(self):
        self.driver.find_element(By.ID,'kw').send_keys('selenium')
        self.driver.find_element(By.ID,'su').click()
        sleep(2)
        self.driver.back()#跳转到一个页面之后再返回到之前的页面
        sleep(2)
        self.driver.refresh()
        sleep(2)
        self.driver.forward()#前进

        self.driver.close() #关闭当前tab
        self.driver.quit() #关闭浏览器


    #浏览器切换
    def test_windows(self):
        self.driver.find_element(By.LINK_TEXT,'新闻').click()
        windows = self.driver.window_handles

        while 1:
            for w in windows:
                self.driver.switch_to.window(w)
                sleep(2)


if __name__ == '__main__':
    case = TestCase()
    # case.test_prop()
    # case.test_method()
    case.test_windows()
