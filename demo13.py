from time import sleep, strftime, localtime, time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    def test1(self):
        self.driver.find_element(By.ID,'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        sleep(2)

        #第一种
        # self.driver.save_screenshot('baidu.png')#会在当前文件所在目录下保存一个图片

        #第二种,将截图加上时间
        # st = strftime('%Y-%m-%d-%H-%M-%S', localtime(time()))#from time import sleep, strftime, localtime, time，调用strftime将时间格式化；localtime(time())：将当前time本地化处理
        # file_name = st + '.png'
        # self.driver.save_screenshot(file_name)
        # self.driver.quit()

        #第三种，将文件保存到一个文件夹里边
        st = strftime('%Y-%m-%d-%H-%M-%S', localtime(time()))#from time import sleep, strftime, localtime, time，调用strftime将时间格式化；localtime(time())：将当前time本地化处理
        file_name = st + '.png'
        path = os.path.abspath('screenshot')
        file_path = path+'/'+file_name
        self.driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    case = TestCase()
    case.test1()