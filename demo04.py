import test.testall
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

#http://sahitest.com/demo/


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')

    def test_webelement_prop(self):
        e = self.driver.find_element(By.ID,'t1')
        e1 = WebElement;
        print(type(e))
        print(e.id)#标示
        print(e.tag_name)#标签名称
        print(e.size)#宽高
        print(e.rect)#宽高和坐标
        print(e.text)#文本内容


    def test_webelement_method(self):
        e = self.driver.find_element(By.ID,'t1')
        e.send_keys('hello world')#输入内容
        sleep(2)
        print(e.get_attribute('type'))#获得属性值
        print(e.get_attribute('name'))
        print(e.get_attribute('value'))

        print(e.value_of_css_property('font'))#css属性值
        print(e.value_of_css_property('color'))

        sleep(2)
        e.clear()#清空内容
        #click()  单击
        #is_selected()  是否被选中
        #is_enabled()  是否可用
        #is_displayed()  是否显示

    def test_method2(self):
        form_element = self.driver.find_element(By.XPATH,'/html/body/form[1]')
        form_element.find_element(By.ID,'t1').send_keys('bala')


if __name__ == '__main__':
    case = TestCase()
    # case.test_webelement_prop()
    # case.test_webelement_method()
    case.test_method2()