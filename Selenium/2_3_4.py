from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()
    # confirm = browser.switch_to.alert
    # confirm.accept()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    z = calc(x)

    input1 = browser.find_element_by_name("text")
    input1.send_keys(z)
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()



finally:
    time.sleep(5)
    browser.quit()