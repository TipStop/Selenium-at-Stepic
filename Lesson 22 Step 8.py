from selenium import webdriver
import time
import os
# import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_element_firstname = browser.find_element_by_name('firstname')
    input_element_firstname.send_keys('firstname')

    input_element_lastname = browser.find_element_by_name('lastname')
    input_element_lastname.send_keys('lastname')

    input_element_email = browser.find_element_by_name('email')
    input_element_email.send_keys('email')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "Test.txt"
    file_path = os.path.join(current_dir, file_name)
    inputfile_element = browser.find_element_by_name('file')
    inputfile_element.send_keys(file_path)

    button_element = browser.find_element_by_tag_name('button')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button_element)
    button_element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
