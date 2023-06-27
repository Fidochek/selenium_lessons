from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '.form-group #input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, '.form-group #answer')
    answer.send_keys(y)

    robotCheckbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    robotCheckbox.click()

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is not None, "Robot radio is not selected by default"

    robotRadiobox = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robotRadiobox.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    time.sleep(4)
    browser.quit()