from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # path = os.path.abspath(__file__)#当前路径，加载form表单需要知道它的路径，__file__代表当前文件的路径
        path = os.path.dirname(os.path.abspath(__file__))#当前路径所在的文件夹
        file_path = 'file:///'+path+'/test_alert.html'#当前本地文件+path路径+文件名称
        print(file_path)
        self.driver.get(file_path)

    def test_alert(self):
        self.driver.find_element(By.ID, 'alert').click()
        #切换到alert
        alert = self.driver.switch_to.alert
        #打印alert里面的文本数据
        print(alert.text)
        sleep(3)
        #点击确定按钮
        alert.accept()

    def test_confirm(self):
        self.driver.find_element(By.ID, 'confirm').click()
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        # confirm.accept() #确定
        sleep(3)
        confirm.dismiss() #取消

    def test_prompt(self):
        self.driver.find_element(By.ID, 'prompt').click()
        sleep(2)
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        sleep(2)
        prompt.send_keys('20')
        sleep(2)
        prompt.accept()
        sleep(3)

if __name__ == '__main__':
    case = TestCase()
    # case.test_alert()
    # case.test_confirm()
    case.test_prompt()
    case.driver.quit()