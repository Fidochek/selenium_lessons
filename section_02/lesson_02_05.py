from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/execute_script.html"

    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    browser.find_element(By.ID, 'answer').send_keys(y)

    browser.find_element(By.ID, 'robotCheckbox').click()

    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.ID, 'robotsRule').click()

    button.click()



finally:
    time.sleep(4)
    browser.quit()