from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math, os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"

    browser.get(link)


    browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('firstname')
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('lastname')
    browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('email')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    browser.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(file_path)

    browser.find_element(By.TAG_NAME, 'button').click()



finally:
    time.sleep(4)
    browser.quit()