import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    image_element = browser.find_element_by_id('treasure')
    valuex_value = image_element.get_attribute('valuex')
    
    answer_value = str(calc(valuex_value))

    input_element = browser.find_element_by_id('answer')
    input_element.send_keys(answer_value)

    checkbox_element = browser.find_element_by_id('robotCheckbox')
    checkbox_element.click()

    radio_element = browser.find_element_by_id('robotsRule')
    radio_element.click()

    button_element = browser.find_element_by_tag_name('button')
    button_element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()