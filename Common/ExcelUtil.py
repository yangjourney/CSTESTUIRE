# -*- coding: utf-8 -*-
import xlrd
import os
class ExcelUtil(object):  
  
    def __init__(self, excelPath, sheetName):  
        self.data = xlrd.open_workbook(excelPath)  
        self.table = self.data.sheet_by_name(sheetName)
        #获取标题 
        self.row = self.table.row_values(0)
        #获取行数  
        self.rowNum = self.table.nrows
        #获取列数 
        self.colNum = self.table.ncols
        #当前列
        self.curRowNo = 1  
          
    def next(self):  
        r = []  
        while self.hasNext():  
            s = {}  
            col = self.table.row_values(self.curRowNo)  
            i = self.colNum  
            for x in range(i):  
                s[self.row[x]] = col[x]  
            r.append(s)  
            self.curRowNo += 1  
        return r         
      
    def hasNext(self):  
        if self.rowNum == 0 or self.rowNum <= self.curRowNo :  
            return False  
        else:  
            return True
    def getCellValue(self, rowIndex, colIndex, xlsFilePath):
        workBook = xlrd.open_workbook(xlsFilePath)
        table = workBook.sheets()[self]
        return table.cell(rowIndex, colIndex).value
#if __name__=='__main__':
#    excel_path = os.path.abspath("D:/CSTESTUIRE/Data/Data.xls")
# 获取对应Excel文件中对应的Sheet，在测试编码过程中进行调整
    #excel = ExcelUtil(excel_path, 'Sheet2')
#    print(ExcelUtil.getCellValue(0, 4, 2, excel_path)) # 获取第一个sheet第四行第二列的单元格的值