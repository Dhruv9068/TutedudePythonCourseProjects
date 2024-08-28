from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('https://www.facebook.com')

emailelement = driver.find_element(By.XPATH, './/*[@id="email"]')
emailelement.send_keys('9412180489')

passelement = driver.find_element(By.XPATH, './/*[@id="pass"]')
passelement.send_keys('##dhruvchaturvedi1&2&3')

login_button = driver.find_element(By.NAME, 'login')
login_button.click()

statuselement = driver.find_element(By.XPATH, "//div[@role=\"button\" and @class=\"x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou\"]")
time.sleep(2)
statuselement.click()

status_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@aria-label=\"What's on your mind, Dhruv?\"]"))
)

status_box.clear()

text_to_type = "hello hi"
for char in text_to_type:
    status_box.send_keys(char)
    time.sleep(0.1)

driver.find_element(By.XPATH, "//span[text()='Post']").click()


