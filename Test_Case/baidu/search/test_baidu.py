# coding=utf-8
'''
Created on 
@author: 
Project:本例中，演示了基本的框架运用方法的实例
'''
import unittest, time, ddt, os
from Common.ExcelUtil import ExcelUtil
from gevent.hub import sleep
from Common.Selenium_Webdriver import webutils

# 获取当前工程目录下的Excel文件，可根据实际情况进行调整
excel_path = os.path.abspath("E:\Web_UI_AutoTest\Data\Data.xls")
# 获取对应Excel文件中对应的Sheet，在测试编码过程中进行调整
excel = ExcelUtil(excel_path, 'Sheet2')

@ddt.ddt
class BaiduTest(unittest.TestCase):
    u"""框架示例"""
    @classmethod
    def setUp(self):
        self.driver = webutils()
        self.driver.max_window()
        sleep (5)  # 隐性等待时间为30秒
        self.base_url = "https://www.baidu.com"

    @ddt.data(*excel.next())
    def test_baidu(self, data):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.send_keys("xpath,.//*[@id='kw']",data['searchcode'])
        driver.click("id,su")
        time.sleep(3)
        title = driver.get_title()
        self.assertEqual(title, data['searchcode'] + u"_百度搜索")
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
