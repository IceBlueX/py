# demo

import openpyxl

# 读表
wb = openpyxl.load_workbook('/Users/libaokun/Desktop/2011国内生产总值.xlsx')

Na = wb.sheetnames
print(Na)

