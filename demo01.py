from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# def test2():
#     driver = webdriver.Chrome()
#     driver.get('https://www.baidu.com/')
#     sleep(1)
#     driver.find_element(By.ID, 'kw').send_keys('selenium')
#     sleep(1)
#     driver.find_element(By.ID, 'su').click()
#     sleep(3)
#     driver.quit()


# def test():
#     import subprocess
#     p = subprocess.Popen("chromedriver")
#     p.communicate()


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def test(self):
        self.driver.get('https://www.baidu.com/')
        sleep(1)
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        sleep(1)
        self.driver.find_element(By.ID, 'su').click()
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    # test()
    case = TestCase()
    case.test()