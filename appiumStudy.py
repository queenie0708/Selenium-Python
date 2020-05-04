
# -*- coding: UTF-8 -*-
import os,time
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

class Test(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'Xiaomi MI MAX3',
            'newCommandTimeout': 240,
            "appActivity": ".app.fragment.main.CivetMainActivity t15929",
            "appPackage": "com.fsc.civetphone",
            "noReset": "true"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test(self):
        print('load success now in test')
        time.sleep(5)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.fsc.civetphone:id/iv_app_border")')
        print('enter survey')
        time.sleep(3) 
        self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.view.View")').click() 
        print('putch card')
        time.sleep(3)
        self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.view.View").text("确定")').click() 
        time.sleep(3)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("btnStart")').click()
        time.sleep(10)

    def tearDown(self):
        time.sleep(10)
        print('now tear down')
        #self.driver.quit()

if __name__=='__main__':
    unittest.main()
