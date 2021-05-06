from selenium import webdriver
import time


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = int(browser.find_element_by_id('num1').text)
    num2 = int(browser.find_element_by_id('num2').text)

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(num1 + num2))

    # ищем элемент с текстом "Python"

    # image_element = browser.find_element_by_id('treasure')
    # valuex_value = image_element.get_attribute('valuex')
    
    # answer_value = str(calc(valuex_value))

    # input_element = browser.find_element_by_id('answer')
    # input_element.send_keys(answer_value)

    # checkbox_element = browser.find_element_by_id('robotCheckbox')
    # checkbox_element.click()

    # radio_element = browser.find_element_by_id('robotsRule')
    # radio_element.click()

    button_element = browser.find_element_by_tag_name('button')
    button_element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()