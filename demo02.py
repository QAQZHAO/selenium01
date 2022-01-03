from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        sleep(1)

    def test_id(self):
        #id是唯一的
        element = self.driver.find_element(By.ID, 'kw')
        element.send_keys('selenium')
        print(type(element))
        # <class 'selenium.webdriver.remote.webelement.WebElement'>

        self.driver.find_element(By.ID, 'su').click()
        sleep(3)
        # self.driver.quit()

    def test_name(self):
        #driver.find_element(By.NAME, 'wd')  这个方法可能返回多个元素，返回第一个
        #self.find_elements(by=by, value=value)  返回一个集合
        self.driver.find_element(By.NAME, 'wd').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        sleep(3)
        self.driver.quit()

    def test_linktext(self):
        self.test_id()
        self.driver.find_element(By.LINK_TEXT,'百度首页').click()
        sleep(3)

    def test_partial_link_text(self):
        self.test_id()
        self.driver.find_element(By.PARTIAL_LINK_TEXT,'首页').click()
        sleep(3)

    def test_xpath(self):
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('极客时间')
        self.driver.find_element(By.ID, 'su').click()
        sleep(3)

    def test_tag(self):
        input = self.driver.find_element(By.TAG_NAME,'input')
        print(input)

    def test_css_selector(self):
        self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys('极客时间')
        self.driver.find_element(By.ID, 'su').click()
        sleep(3)

    def test_class_name(self):
        self.driver.find_element(By.CLASS_NAME,'s_ipt').send_keys('极客时间')
        self.driver.find_element(By.ID, 'su').click()
        sleep(3)

if __name__ == '__main__':
    case = TestCase()
    # case.test_id()
    # case.test_name()
    # case.test_linktext()
    # case.test_partial_link_text()
    # case.test_xpath()
    # case.test_tag()
    # case.test_css_selector()
    case.test_class_name()