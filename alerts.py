# import time
# from selenium import webdriver

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("--disable-notifications")

# driver = webdriver.Chrome(options=opts)
# driver.maximize_window()

# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)

# driver.find_element('xpath', '//button[@id="alertBtn"]').click()
# time.sleep(2)

# alert = driver.switch_to.alert
# alert.accept()
# time.sleep(2)
# driver.quit()

# ------------------------------------------------------------
# import time
# from selenium import webdriver

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=opts)
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)

# driver.find_element('xpath', '//button[@id="promptBtn"]').click()

# alert = driver.switch_to.alert
# alert.send_keys('Shahida')
# time.sleep(2)
# alert.accept()

# --------------------------------------------------------------
import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

file_path = '/Users/shahidakhan/Desktop/Ramya_selenium_training/Shahida/Python Roadmap.pdf'

driver.find_element('xpath', '//input[@id="singleFileInput"]').send_keys(file_path)
