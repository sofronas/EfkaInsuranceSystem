#=========================================#
# Sofron Insurance Printing System EFKA   #
# Email: sofronas.konstantinos@gmail.com  #
# Name: Sofronas Konstantinos Sotirios    #
# Website: https://sofronas.github.io     #
#=========================================#

#Libraries
#
import os
import time
import random
import getpass
import smtplib
import string
import sys
import fileinput
import urllib2
import getpass
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#-----------------------------------------------------
#Functions

global taxis_net_username
global taxis_net_password
global amka_number

taxis_net_username = ""
taxis_net_password = ""
amka_number = ""

global url
global browser

url = "https://www.idika.org.gr/EfkaServices/"

print("Internet OKAY")
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", os.getcwd())
profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf") #"application/pdf"
firefox_mozilla = webdriver.Firefox(firefox_profile = profile)
browser = firefox_mozilla

browser.get(url)

eisodos_button = browser.find_element_by_id("ContentPlaceHolder1_btnEisodos")
time.sleep(2)
eisodos_button.click()
print("Eisodos OKAY")
time.sleep(2)

taxis_net_button = browser.find_element_by_id("ContentPlaceHolder1_btnGGPSAuth_CD")
time.sleep(0.5)
taxis_net_button.click()
print("Forward to taxis.net")
time.sleep(2)

taxis_xristis = browser.find_element_by_id("v")
time.sleep(0.5)
taxis_xristis.send_keys(taxis_net_username)
print("Username was given")
time.sleep(1)

taxis_pass = browser.find_element_by_id("j_password")
time.sleep(0.5)
taxis_pass.send_keys(taxis_net_password)
time.sleep(1)

taxis_login_button = browser.find_element_by_class_name("submit-button")
time.sleep(0.5)
taxis_login_button.click()
print("Login to taxis.net")
time.sleep(2)

try:
    tmp = browser.find_element_by_class_name("submit-button")
    if tmp is not None:
        taxis_send_button = tmp
        time.sleep(0.5)
        taxis_send_button.click()
        print("Egkrisi OKAY")
        time.sleep(2)
    else:
        print("Egkrisi not OKAY")
except:
    print("except was caugth")
    pass

amka_input = browser.find_element_by_id("ContentPlaceHolder1_ASPxFormLayout1_ASPxFormLayout1_E1AMKA_I")
time.sleep(0.5)
amka_input.send_keys(amka_number)
print("Amka was Given")

amka_login_button = browser.find_element_by_id("ContentPlaceHolder1_ASPxFormLayout1_ASPxFormLayout1_E2btnEisodos")
time.sleep(0.5)
amka_login_button.click()
print("Amka button was clicked")
time.sleep(2)

try:
    time.sleep(2)
    eisfores_href = browser.find_element_by_id("ContentPlaceHolder1_panelOikEkkr_OikonomikesEkremmotitesPanel_EisforaPanel_BootstrapFormLayout2_contrLink")
    print("Page is ready")
    eisfores_href.click()
except TimeoutException as identifier:
    print("Loading took too much time")
    print(identifier)

try:
    pdf_b = browser.find_element_by_id("ContentPlaceHolder1_panelEidop_mainFormLayout_btnEidopoiitirio")
    pdf_b.click()
except TimeoutException:
    print("Loading took too much time")


window_before = browser.window_handles[0]
window_after = browser.window_handles[1]
time.sleep(2)

browser.close()
browser.switch_to_window(window_after)

print("Efka DONE")

time.sleep(100)
browser.quit()
