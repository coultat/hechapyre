from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from login import login
import time
from selenium.webdriver.common.action_chains import ActionChains


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
    master_data_nav = browser.find_element_by_xpath(
            "/html/body/form[1]/div[27]/div[2]/div[1]/div[2]/div/table/tbody/tr/td[1]/div")
    action = ActionChains(browser)
    action.move_to_element(master_data_nav).perform()
    for i in range(10):
        try:
            browser.find_element_by_xpath("/html/body/div[4]/table/tbody/tr[9]/td/div").click()
            break
        except:
            time.sleep(1)
    return browser


def writing_the_placement_name_and_go(browser, placement = "yieldlove.com_d_300x250_1"):
    iframe = browser.find_elements_by_tag_name("iframe")
    for i in range(1, 500):
        try:
            browser.find_element_by_id("rulesFilternameValue").send_keys(placement)
            for x in range(50):
                try:
                    browser.find_element_by_id("button_global;global.button.filter").click()
                    break
                except:
                    time.sleep(1)
            break
        except:
            browser.switch_to.default_content()
            browser.switch_to.frame(iframe[i])
    return browser


def deleting_rules(browser, placement = "yieldlove.com_d_300x250_14"):
    aux = 0
    for i in range(1, 50):
        try:
            if browser.find_element_by_xpath(
                            '/html/body/form/div[7]/div[4]/table/tbody/tr['+str(i)+']/td[1]/div/span'
                                        ).text == placement and browser.find_element_by_xpath(
                            '/html/body/form/div[7]/div[4]/table/tbody/tr['+str(i)+']/td[4]/div/span'
                                        ).text == 'Expired':
                browser.find_element_by_xpath('/html/body/form/div[7]/div[4]/table/tbody/tr['+str(i)+']/td[7]/div').click()
                print("aquí nao funcionou***************************************************")
                obj = browser.switch_to.alert
                obj.accept()
                aux = 1
                break
        except:
            pass
    return browser, aux


def deleting_name_from_field(browser):
    for i in range(1, 20):
        try:
            browser.find_element_by_id("rulesFilternameValue").send_keys(Keys.CONTROL, "a")
            browser.find_element_by_id("rulesFilternameValue").send_keys(Keys.BACKSPACE)
            break
        except:
            time.sleep(1)

def main_delete(placements):
    browser = login_adtech()
    time.sleep(8)
    action = ActionChains(browser)
    browser = select_adtech_rules(browser)
    time.sleep(5)
    y = 0
    for placement in placements:
        y += 1
        print(placement, y)
        aux = 0
        browser = writing_the_placement_name_and_go(browser, placement)
        time.sleep(1)
        browser, aux = deleting_rules(browser, placement)
        deleting_name_from_field(browser)
    browser.close()