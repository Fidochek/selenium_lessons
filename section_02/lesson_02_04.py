from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
button.click()