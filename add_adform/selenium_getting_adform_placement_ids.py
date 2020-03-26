from selenium import webdriver
from store.login import login
from selenium.webdriver.common.keys import Keys
from store.adform_problems import placements_ids as placements
import time


def login_adform():
    browser = webdriver.Firefox()
    browser.get(login.url)
    browser.find_element_by_name("username").send_keys(login.user)
    browser.find_element_by_name("password").send_keys(login.password)
    browser.find_element_by_name("button").click()
    return browser


def selecting_inventory(browser):
    browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/a[2]").click()
    return browser


def writing_placement_and_enter(browser, placement):
    search = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/div/div/div[2]/common-search-2/div/div/input")
    search.send_keys(placement)
    search.send_keys(Keys.RETURN)


def deleting_placement_name(browser):
    search = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/div/div/div[2]/common-search-2/div/div/input")
    search.send_keys(Keys.CONTROL, "a")
    search.send_keys(Keys.BACKSPACE)


def fetching_id(browser, placement, helper):
    try:
        placement_id = browser.find_element_by_xpath('/html/body/div[4]/div/div[3]/div/div/div/div/div/div[3]/table/tbody/tr/td[2]').text
        if placement_id == helper:
            time.sleep(5)
            placement_id = browser.find_element_by_xpath(
                '/html/body/div[4]/div/div[3]/div/div/div/div/div/div[3]/table/tbody/tr/td[2]').text
        helper = placement_id
        return placement, placement_id, helper
    except:
        return placement, 'THERE IS NO PLACEMENT', helper


final = []
browser = login_adform()
time.sleep(15)
selecting_inventory(browser)
i = 0
time.sleep(5)
helper = ''
for placement in placements:
    writing_placement_and_enter(browser, placement[0])
    time.sleep(1)
    placement_name, placement_id, helper = fetching_id(browser, placement, helper)
    final.append([placement[0], placement[1], placement_id])
    deleting_placement_name(browser)

print(final)
'''
f = open('placements_adformId.py', 'a+')
for data in final:
    fwrite(f'{data[0]} - {data[1]}')
'''