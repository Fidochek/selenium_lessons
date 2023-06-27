

alert = browser.switch_to.alert
alert.accept()


alert = browser.switch_to.alert
alert_text = alert.text

confirm = browser.switch_to.alert
confirm.dismiss()

prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()