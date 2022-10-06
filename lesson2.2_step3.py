from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import time


try: 
    link = " http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    el_1 = browser.find_element(By.CSS_SELECTOR, '[id="num1"]')
    x1 = int(el_1.text)
    
    el_2 = browser.find_element(By.CSS_SELECTOR, '[id="num2"]')
    x2 = int(el_2.text)
    x = str(x1 + x2)
    
    #select1 = browser.find_element(By.TAG_NAME, "select")
    #select1 = Select(browser.find_element(By.TAG_NAME, "select"))
    #select.select_by_value('x') # ищем элемент
    #select1.send_keys(x)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value=x)
   
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
 

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()