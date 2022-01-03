from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # path = os.path.abspath(__file__)#当前路径，加载form表单需要知道它的路径，__file__代表当前文件的路径
        path = os.path.dirname(os.path.abspath(__file__))#当前路径所在的文件夹
        file_path = 'file:///'+path+'/forms.html'#当前本地文件+path路径+文件名称
        print(file_path)
        self.driver.get(file_path)

    def test_login(self):
        username = self.driver.find_element(By.ID,'username')
        username.send_keys('admin')
        pwd = self.driver.find_element(By.ID,'pwd')
        pwd.send_keys('123')
        print(username.get_attribute('value'))#输出username的值
        print(pwd.get_attribute('value'))

        sleep(2)
        self.driver.find_element(By.ID,'submit').click()
        self.driver.switch_to.alert.accept()#消除alert

        username.clear()#清空username
        pwd.clear()
        sleep(2)
if __name__ == '__main__':
    case = TestCase()
    case.test_login()
