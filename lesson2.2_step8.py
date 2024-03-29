from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    time.sleep(4) 
    browser.get(link)

    
    
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys("Ivan")
   
    input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input2.send_keys("Petrov")
    
    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input3.send_keys("z@et.ru")
   

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'irara.txt')
    element =  browser.find_element(By.CSS_SELECTOR, '[name="file"]')
    element.send_keys(file_path)

   
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла