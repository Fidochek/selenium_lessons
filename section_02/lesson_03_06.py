from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math, os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'

    browser.get(link)

    browser.find_element(By.TAG_NAME, 'button').click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.ID, 'input_value')
    x.get_attribute()

    y = calc(x)

    browser.find_element(By.ID, 'answer').send_keys(y)

    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.quit()

