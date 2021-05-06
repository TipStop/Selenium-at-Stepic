import math
from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_value = browser.find_element_by_id('input_value').text

    input_element = browser.find_element_by_id('answer')
    input_element.send_keys(str(calc(x_value)))

    checkbox_element = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox_element)
    checkbox_element.click()

    radio_element = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_element)
    radio_element.click()

    button_element = browser.find_element_by_tag_name('button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_element)
    button_element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
