import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# y = calc(x)
# x = 1
try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id('input_value').text
    answer_value = str(calc(x))

    answer_element = browser.find_element_by_id('answer')
    answer_element.send_keys(answer_value)

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

assert y != y, y