from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # path = os.path.abspath(__file__)#当前路径，加载form表单需要知道它的路径，__file__代表当前文件的路径
        path = os.path.dirname(os.path.abspath(__file__))#当前路径所在的文件夹
        file_path = 'file:///'+path+'/forms2.html'#当前本地文件+path路径+文件名称
        print(file_path)
        self.driver.get(file_path)

    def test_checkbox(self):
        swimming = self.driver.find_element(By.NAME, 'swimming')
        if not swimming.is_selected():  # 如果没有被选中，才去选中
            swimming.click()
        reading = self.driver.find_element(By.NAME, 'reading')
        if not reading.is_selected():
            reading.click()
        sleep(3)
        swimming.click()
        sleep(5)
        self.driver.quit()

    def test_radio(self):
        lst = self.driver.find_elements(By.NAME, 'gender')
        # lst[0].click()
        lst[1].click()



if __name__ == '__main__':
    case = TestCase()
    # case.test_checkbox()
    case.test_radio()