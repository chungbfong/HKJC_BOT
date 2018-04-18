from selenium import webdriver
import time
import subprocess
import sys
from cmd import Cmd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# example.py
driver = webdriver.Chrome()
driver.get("http://bet.hkjc.com/")
driver.implicitly_wait(5)
if(driver.find_element_by_id('iframeDisplay')):
     print("hi")
