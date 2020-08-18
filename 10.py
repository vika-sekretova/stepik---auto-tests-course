from selenium import webdriver
import time
import math
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("Ivanov")
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("i@mail.ru")

    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    id_file = browser.find_element_by_css_selector("#file")
    id_file.send_keys(file_path)     
       
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
   
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
   # time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла