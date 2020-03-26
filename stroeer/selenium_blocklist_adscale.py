from create_placements_stroeer_ssp import transforming_placements_json, transforming_websites_json, merging_placements_websites
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from store.sample import placements
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from store.login import login
import time


def login_adscale():
    driver = webdriver.Firefox()
    driver.get(login.adscale_url)
    time.sleep(10)
    driver.find_element_by_id('username').send_keys(login.adscale_user)
    driver.find_element_by_id('password').send_keys(login.adscale_pw)
    driver.find_element_by_id('id7').click()
    return driver


d = login_adscale()