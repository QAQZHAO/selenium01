from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
from selenium.webdriver.support.select import Select


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # path = os.path.abspath(__file__)#当前路径，加载form表单需要知道它的路径，__file__代表当前文件的路径
        path = os.path.dirname(os.path.abspath(__file__))#当前路径所在的文件夹
        file_path = 'file:///'+path+'/forms3.html'#当前本地文件+path路径+文件名称
        print(file_path)
        self.driver.get(file_path)

    def test_select(self):
        se = self.driver.find_element(By.ID, 'provise')
        select = Select(se)
        # select.select_by_index(2)#通过索引来定位，第三个索引就是2
        # sleep(2)
        # select.select_by_value('bj')#通过value值来定位
        # sleep(2)
        # select.select_by_visible_text('TianJin')  # 通过可视化文本来定位
        # sleep(2)


        #循环选中所有选项，然后再反选
        # for i in range(3):
        #     select.select_by_index(i)
        #     sleep(1)
        # sleep(3)
        #
        # select.deselect_all()#反选
        #
        # sleep(3)
        #

        # 输出当前option所有标签
        for option in select.options:
           print(option.text)

        self.driver.quit()

        # deselect_by_value()  根据值反选
        # deselect_by_index()  根据索引反选
        # deselect_by_visible_text()  根据文本反选
        # all_selected_options  所有选中的选项
        # first_selected_option  第一个选择选项






if __name__ == '__main__':
    case = TestCase()
    case.test_select()