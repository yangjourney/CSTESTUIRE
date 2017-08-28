# coding=utf-8
import unittest,os,time
from Common.Selenium_Webdriver import webutils
from Common.Excel_R import getCellValue
from Common.log import logger

excel_path = os.path.abspath("D:/CSTESTUIRE/Data/Data.xls")
class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.autoDriver = webutils()
        self.autoDriver.max_window()
        self.base_url= "http://10.2.5.139:9000/#/login"
        self.autoDriver.get(self.base_url)
        self.autoDriver.wait(5)
        self.autoDriver.send_keys("xpath|"+getCellValue(0, 1, 2, excel_path), "test01")
        self.autoDriver.send_keys("xpath|"+getCellValue(0, 2, 2, excel_path), "123456")
        self.autoDriver.click("xpath|.//parent::button")
        logger.info('登录成功！')

    def test_1Search(self):
        self.autoDriver.click("xpath|"+getCellValue(0, 4, 2, excel_path))
        self.autoDriver.click("xpath|"+getCellValue(0, 5, 2, excel_path))
        self.autoDriver.send_keys("xpath|"+getCellValue(0, 6, 2, excel_path), "李维辉")
        self.autoDriver.send_keys("xpath|"+getCellValue(0, 7, 2, excel_path), "")
        self.autoDriver.send_keys("xpath|"+getCellValue(0, 8, 2, excel_path), "")
        self.autoDriver.click("xpath|"+getCellValue(0, 9, 2, excel_path))
        logger.info('查询出符合条件的记录！数据校验中...')
		#logger.info('断言后续添加，暂无时间去弄...')
        #try:
        #    self.assertEqual(u"预期结果", self.autoDriver.title)
        #except AssertionError as e:
        #    print(u"不一致")
        #    logger.info('数据不一致，测试失败。')
    time.sleep(5)

    def test_2Rest(self):
        self.autoDriver.click("xpath|"+getCellValue(0, 4, 2, excel_path))
        self.autoDriver.click("xpath|"+getCellValue(0, 5, 2, excel_path))
        self.autoDriver.send_keys("xpath|"+getCellValue(0, 6, 2, excel_path), "潘献军")
        self.autoDriver.send_keys("xpath|"+getCellValue(0, 7, 2, excel_path), "")
        self.autoDriver.send_keys("xpath|"+getCellValue(0, 8, 2, excel_path), "")
        self.autoDriver.click("xpath|"+getCellValue(0, 10, 2, excel_path))
        logger.info('成功执行重置操作！')
        time.sleep(5)

    @classmethod
    def tearDownClass(self):
        self.autoDriver.quit()


