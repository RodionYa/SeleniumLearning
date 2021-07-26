from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
         EC.text_to_be_present_in_element(
             (By.ID, "price"), "$100"))
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    z = calc(x)
    input1 = browser.find_element_by_name("text")
    input1.send_keys(z)
    button = browser.find_element_by_css_selector("id=solve")
    button.click()

finally:
    time.sleep(5)
    browser.quit()