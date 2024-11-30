import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



def test_invoke_browser1():
    global driver
    driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Driver\\chromedriver.exe")
    driver.get("https://www.flipkart.com")
    driver.implicitly_wait(2)
    driver.maximize_window()

def test_login():
    driver.find_element_by_xpath("//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[2]/div[2]/div/div/div/div/a/span").click()
    driver.find_element_by_xpath("//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input").send_keys("9890029546")
    driver.find_element_by_xpath("//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[3]/button").click()
    driver.find_element_by_xpath("//*[@id="container"]/div/div[3]/div/div[2]/div/div/form/button").click()