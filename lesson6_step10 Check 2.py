from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
    input3.send_keys("email")
    input4 = browser.find_element_by_css_selector("[placeholder='Input your phone:']")
    input4.send_keys("Russia")
    input3 = browser.find_element_by_css_selector("[placeholder='Input your address:']")
    input3.send_keys("address")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.txt

    assert "Congratulations! You have successfully registred!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()


