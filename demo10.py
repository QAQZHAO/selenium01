from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # path = os.path.abspath(__file__)#当前路径，加载form表单需要知道它的路径，__file__代表当前文件的路径
        # path = os.path.dirname(os.path.abspath(__file__))#当前路径所在的文件夹
        # file_path = 'file:///'+path+'/test_wait.html'#当前本地文件+path路径+文件名称
        # print(file_path)

        path = 'file:///'+os.path.abspath('test_wait.html')
        self.driver.get(path)

    def test(self):
        self.driver.find_element(By.ID,'button').click()
        #显示等待
        wait = WebDriverWait(self.driver,3)
        wait.until(EC.text_to_be_present_in_element((By.ID,'id2'),'id2')) #from selenium.webdriver.support import expected_conditions as EC，查看expected_conditions，传入定位器+test文本
        print(self.driver.find_element(By.ID, 'id2').text)#找到id2并打印出来
        print('OK')

if __name__ == '__main__':
    case = TestCase()
    case.test()