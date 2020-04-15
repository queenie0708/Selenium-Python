from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://icivetapps.foxconn.com/iapps/VoteSystem/Secrecy/Index/WH2020?lang=cn")
for i in range(3):
    print(str(i) + 'sec')
    time.sleep(1)
driver.find_element_by_xpath('//*[@id="topdiv"]/div[2]/a').click()
print('login licked')
for i in range(3):
    print(str(i) + 'sec')
    time.sleep(1)
driver.find_element_by_id("UserId").send_keys('H0135701')
driver.find_element_by_id("Password").send_keys('19900708')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="main"]/div[2]/form[2]/table/tbody/tr[4]/td/input').click()
time.sleep(3)
driver.close()

