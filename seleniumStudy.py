## 引入WebDriver的包
from selenium import webdriver

## 创建浏览器对象
browser = webdriver.Chrome()

## 打开百度网站
browser.get('https://www.baidu.com/')
