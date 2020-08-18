from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
     
    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option2.click()
       
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