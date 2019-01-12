from selenium import webdriver

browser = webdriver.Chrome()  
browser.get('file://10.75.10.81/Share/Dynamo2/CTS/V0.520/STS/results/2019.01.10_09.38.27/test_result_failures.html')  
testNames = browser.find_elements_by_class_name('testname')
details = browser.find_elements_by_class_name('details')

for test in testNames:
  print(test.text)
print('==========================================below is details===========================')
for detail in details:
  print(detail.text)

browser.quit()

