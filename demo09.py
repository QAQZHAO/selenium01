from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        # sleep(2)

    def test_sleep(self):
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        sleep(2) # 线程的阻塞 blocking wait
        self.driver.find_element(By.ID, 'su').click()
        sleep(3)
        self.driver.quit()

    def test_implicitly(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        self.driver.quit()

    def test_wait(self):
        wait = WebDriverWait(self.driver,2)#from selenium.webdriver.support.wait import WebDriverWait
        wait.until(EC.title_is('百度一下，你就知道'))#from selenium.webdriver.support import expected_conditions as EC
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    # case.test_sleep()
    # case.test_implicitly()
    case.test_wait()