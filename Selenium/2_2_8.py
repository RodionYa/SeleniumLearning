from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Rodion")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Yasinovsky")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("sbsp_-@mail.ru")
    file_button = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'Newfile.txt')  # добавляем к этому пути имя файла

    file_button.send_keys(file_path)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    time.sleep(5)
    browser.quit()