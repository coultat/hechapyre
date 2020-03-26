from selenium import webdriver
from login import login
import time
from selenium.webdriver.common.action_chains import ActionChains
from store.store_prebid_placements import placements_a as placements


def login_adtech():
    browser = webdriver.Firefox()
    browser.get(login.url)
    for i in range(15):
        try:
            browser.find_element_by_id("callback_0").send_keys(login.user)
            break
        except:
            time.sleep(1)
    browser.find_element_by_name("callback_2").click()
    for i in range(10):
        try:
            browser.find_element_by_name("callback_1").send_keys(login.password)
            break
        except:
            time.sleep(1)
    browser.find_element_by_name("callback_2").click()
    return browser


def select_adtech_rules(browser):
    master_data_nav =  browser.find_element_by_xpath("/html/body/form[1]/div[27]/div[2]/div[1]/div[2]/div/table/tbody/tr/td[1]/div")
    action = ActionChains(browser)
    action.move_to_element(master_data_nav).perform()
    for i in range(10):
        try:
            browser.find_element_by_xpath("/html/body/div[4]/table/tbody/tr[9]/td/div").click()
            break
        except:
            time.sleep(1)
    return browser


if __name__ == '__main__':
    placements = ['yieldlove.com_d_300x250_1']
    for placement in placements:
        browser = login_adtech()
        time.sleep(10)
        browser = select_adtech_rules(browser)



