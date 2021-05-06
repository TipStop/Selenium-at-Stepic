from selenium import webdriver
import time
import os
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_element = browser.find_element_by_tag_name('button')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button_element)
    button_element.click()

    time.sleep(2)

    alert = browser.switch_to.alert
    alert.accept()

    time.sleep(2)

    x_value = browser.find_element_by_id('input_value').text

    input_element = browser.find_element_by_id('answer')
    input_element.send_keys(str(calc(x_value)))

    button_element = browser.find_element_by_tag_name('button')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button_element)
    button_element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
