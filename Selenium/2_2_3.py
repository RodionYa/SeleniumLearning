from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/selects2.html"

def calc(x,y):
    return str(int(x)+int(y))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text

    z = calc(x,y)
    print(z)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()
finally:
    time.sleep(5)
    browser.quit()
