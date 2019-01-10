import xlrd
import xlwt
import os
from paoerful.class_tax import Tax
import time

file_name = '\\'+'test.xlsx'

openfile = xlrd.open_workbook(os.getcwd()+file_name)

print(openfile.sheet_names())

sheet = openfile.sheet_by_index(0)
tax_code = sheet.col_values(0)[1:]


def set_style(name,height,bold=False):
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = name # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

new_xl = xlwt.Workbook()
new_sheet = new_xl.add_sheet('sheet1',cell_overwrite_ok=True)

for i  in range(len(tax_code)):
    start = time.time()
    new_sheet.write(i,0,tax_code[i], set_style('Arial',220,True))
    t = Tax(tax_code[i])
    new_sheet.write(i,1,t.taxx, set_style('Arial', 220, True))
    end = time.time()
    print('共有：%s 个' %len(tax_code) + '正在No: %s' % str(i) + '上一个耗时:%s'%(end-start))

new_xl.save('test2.xls')