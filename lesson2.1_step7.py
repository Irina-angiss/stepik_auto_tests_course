from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    box = browser.find_element(By.ID, "treasure")
    x = box.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input1.send_keys(y)
    
    #чекбокс
    option1 = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    option1.click()
    
    #чрадиобаттон
    option2 = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
    option2.click()
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
 

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()