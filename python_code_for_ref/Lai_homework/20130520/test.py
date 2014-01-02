import os
import time
print(os.times())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))


import ctypes          #windows message
MessageBox = ctypes.windll.user32.MessageBoxA #python 2.x
MessageBox = ctypes.windll.user32.MessageBoxW #python 3.x
'''
MessageBox(None, 'Excel_merge finish', 'Window title', 0)
MessageBox(None, 'Excel_merge finish', 'Window title', 1)
MessageBox(None, 'Excel_merge finish', 'Window title', 2)
MessageBox(None, 'Excel_merge finish', 'Window title', 4)
MessageBox(None, 'Excel_merge finish', 'Window title', 5)
MessageBox(None, 'Excel_merge finish', 'Window title', 6)
'''






import time
import sys

toolbar_width = 40

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("\n")







a = 5
b = -3

c = b - a

print(c)



a = "5"
b = "-3"

c = int(b) - int(a)

print(c)


'''
import xlwt3 as xlwt

x=1
y=2
z=3

list1=[2.34,4.346,4.234]

book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet("Sheet 1")

sheet1.write(0, 0, "Display")
sheet1.write(1, 0, "Dominance") 
sheet1.write(2, 0, "Test")

sheet1.write(0, 1, x)
sheet1.write(1, 1, y)
sheet1.write(2, 1, z)

sheet1.write(4, 0, "Stimulus Time")
sheet1.write(4, 1, "Reaction Time")

i=4

for n in list1:
    i = i+1
    sheet1.write(i, 0, n)



book.save("trial.xls")
'''

import xlwt3 as xlwt
from datetime import datetime

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                     num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0, 0, 1234.56, style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))

wb.save('example.xls')