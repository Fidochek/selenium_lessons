from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.ID, 'treasure')
    x = treasure.get_attribute('valuex')
    print(x)

    y = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    robotCheckbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    robotCheckbox.click()

    robotRadiobox = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robotRadiobox.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(4)
    browser.quit()