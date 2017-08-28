# coding=utf-8
from Common.Excel_R import getCellValue

def search(self, Legal, Business,Phone,excel_path):
    #driver=self.driver
    self.driver.wait(5)
    self.driver.click("xpath|"+getCellValue(0, 4, 2, excel_path))
    self.driver.click("xpath|"+getCellValue(0, 5, 2, excel_path))
    self.driver.send_keys("xpath|"+getCellValue(0, 6, 2, excel_path), Legal)
    self.driver.send_keys("xpath|"+getCellValue(0, 7, 2, excel_path), Business)
    self.driver.send_keys("xpath|"+getCellValue(0, 8, 2, excel_path), Phone)
    self.driver.click("xpath|"+getCellValue(0, 9, 2, excel_path))
