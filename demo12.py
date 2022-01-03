from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    def test1(self):
        self.driver.execute_script("alert('test')")
        sleep(2)
        self.driver.switch_to.alert.accept()

    def test2(self):
        #通过JS打印标题
        js = 'return document.title'
        title = self.driver.execute_script(js)
        print(title)

    def test3(self):
        # 通过JS修改百度输入框的样式
        js = 'var q = document.getElementById("kw");q.style.border="2px solid red"'#var q=document.getElementById("kw")：定义一个变量查询；q.style.border="2px：给他一个边框；solid：表示一个实体
        self.driver.execute_script(js)#执行一下这个js

    def test4(self):
        self.driver.find_element(By.ID,'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        sleep(2)
        #滚动
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute_script(js)  # 执行一下这个js
        sleep(2)

if __name__ == '__main__':
    case = TestCase()
    # case.test1()
    # case.test2()
    # case.test3()
    case.test4()

