from selenium import webdriver

browser = webdriver.Chrome()  #指定selenium进行自动化操作时选用谷歌浏览器
browser.get('https://www.imdb.com/movies-in-theaters/')  
total_book = browser.find_element_by_id('main')  
books = total_book.find_elements_by_class_name('outline')   
i = 1
for book in books:  
    print (str(i)+ book.text + '\n')    
    i += 1
browser.quit() 
