#coding=utf-8
import sys

from selenium.webdriver.common.by import By

reload(sys)
sys.setdefaultencoding('utf-8')
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("http://172.19.80.72/invest-research-web/login")
browser.find_element_by_id("account").send_keys("ceshi17")
time.sleep(1)
browser.find_element_by_id("password").send_keys("11111111")
time.sleep(1)
browser.find_element_by_id("loginBtn").click()
time.sleep(3)
# browser.quit()

# actions = ActionChains(browser)
# actions.move_to_element(input_loginBtn)
# actions.click(input_loginBtn)
# actions.perform()

# login in
list = []
menuList = browser.find_elements_by_class_name("sidebar-item")
for menu in menuList:
    if menu.get_attribute("href"):
        list.append(menu.get_attribute("href"))
        # menu.find_element_by_class_name("sidebar-name").click()
        # time.sleep(1)
    else:
        continue

for item in list:
    if("http" in item):
        browser.get(item+"")
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"ifind-loading-img")))
        time.sleep(1)

# print(menuList.get_attribute("href"))

browser.get("http://172.19.80.72/invest-research-web/logout")

# browser.close()