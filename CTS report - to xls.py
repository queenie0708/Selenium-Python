#from selenium import webdriver
import xlwt

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheetNames = ['CTS','GTS','VTS','GSI']

for sheetName in sheetNames:
  sheet = book.add_sheet(sheetName)
  sheet.write(0, 0, 'No.')  # 其中的'0-行, 0-列'指定表中的单元
  sheet.write(0, 1, 'Module')
  sheet.write(0, 2, 'Test')
  sheet.write(0, 3, 'Result')
  sheet.write(0, 4, 'Details')
  sheet.write(0, 5, 'ErrorID:')
book.save(r'D:\test\test1.xls')  # 在字符串前加r，声明为raw字符串，这样就不会处理其中的转义了。否则，可能会报错

# browser = webdriver.Chrome()
# browser.get('file://10.75.10.81/Share/ANT/CTS/V0.250/CTS/results/2018.12.18_13.39.28/test_result_failures.html')
# testNames = browser.find_elements_by_class_name('testname')
# details = browser.find_elements_by_class_name('details')
#
# for test in testNames:
#   print(test.text)
# print('==========================================below is details===========================')
# for detail in details:
#   print(detail.text)
# browser.quit()
