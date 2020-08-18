from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1_element = browser.find_element_by_css_selector("#num1")
    num1 = num1_element.text
    n1 = int(num1)
    num2_element = browser.find_element_by_css_selector("#num2")
    num2 = num2_element.text
    n2 = int(num2)
    sum = n1 + n2
    s = str(sum)
    #browser.find_element_by_tag_name("select").click()
    #browser.find_element_by_css_selector("[value=s]").click()
    
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(s)

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