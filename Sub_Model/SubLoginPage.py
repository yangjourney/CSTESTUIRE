# coding=utf-8
from Base_Model.BasePage import BasePage
from Common.Excel_R import getCellValue

class SubLoginPage(BasePage):
    def __init__(self, driver, baseUrl):
        """
        :param driver:
        :param baseUrl:
        """
        # 调用其 基类 BasePage的 构造函数
        # 实现 基类 的构造函数的功能
        super().__init__(driver, baseUrl)
        self.loginPageUrl = "login"
        self.driver.clearCookies()


    def login(self, userName, password,excel_path):
        self.openPage(self.loginPageUrl)
        # self.driver.clearCookies()
        self.driver.wait(5)
        self.driver.send_keys("xpath|"+getCellValue(0, 1, 2, excel_path), userName)
        self.driver.send_keys("xpath|"+getCellValue(0, 2, 2, excel_path), password)
        self.driver.click("xpath|.//parent::button")

    def getMainPage(self):
        return self.baseUrl
