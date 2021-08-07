from selenium import webdriver
import math
import time
import pytest


link_1 = "https://stepik.org/lesson/236895/step/1"
link_2 = "https://stepik.org/lesson/236896/step/1"
link_3 = "https://stepik.org/lesson/236897/step/1"
link_4 = "https://stepik.org/lesson/236898/step/1"
link_5 = "https://stepik.org/lesson/236899/step/1"
link_6 = "https://stepik.org/lesson/236903/step/1"
link_7 = "https://stepik.org/lesson/236904/step/1"
link_8 = "https://stepik.org/lesson/236905/step/1"

links = [link_1, link_2, link_3, link_4, link_5, link_6, link_7, link_8]


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', links)
def test_correct_text(browser, link):
    answer = str(math.log(int(time.time())))
    browser.get(link)
    input1 = browser.find_element_by_tag_name("textarea")
    input1.send_keys(answer)
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    text_element = browser.find_element_by_css_selector("pre.smart-hints__hint")
    out_text = text_element.text

    assert out_text == 'Correct!', f"Output text: {out_text}, but expected: Correct!"
