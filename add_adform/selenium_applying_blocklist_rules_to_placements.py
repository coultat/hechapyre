from selenium import webdriver
from store.login import login
from store.websites_to_whitelist import websites
from store.adform_problems import placements_ids
#from selenium.webdriver.common.keys import Keys
#from all_placements import best_placements as placements
import time


def login_adform():
    browser = webdriver.Firefox()
    browser.get(login.url)
    browser.find_element_by_name("username").send_keys(login.user)
    browser.find_element_by_name("password").send_keys(login.password)
    browser.find_element_by_name("button").click()
    return browser


def select_inventory(browser):
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/a[2]').click()
    for i in range(10):
        try:
            browser.find_element_by_xpath("/html/body/div[3]/div/ul/li[4]/a").click()
            break
        except:
            time.sleep(1)
    for i in range(10):
        try:
            browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[1]/ul/div/ul/li[2]/div/a').click()
            break
        except:
            time.sleep(1)
    return browser


def select_website_name(browser, websites, amount_of_websites):
    final = []
    for i in range(1, 1000):
        website_name = ''
        print(i)
        try:
            website_obj = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/section[2]/div/section[1]/div/div/table/tbody/tr['+str(i)+']/td[1]')
            if website_obj.text in websites:
                print(website_obj.text)
                website_obj.click()
                browser.find_element_by_xpath(
                   "/html/body/div[3]/div/div[2]/div/section[2]/div/section[2]/form/div/header/ul/li[2]/a"
                ).click()
                try:
                    print("try")
                    placements_checklist = browser.find_element_by_xpath(
                        "/html/body/div[3]/div/div[2]/div/section[2]/div/section[2]/form/div/main/div[2]/div/div/div/div[1]/div[2]"
                    ).text
                except:
                    print("except")
                    placements_checklist = browser.find_element_by_xpath(
                        "/html/body/div[3]/div/div[2]/div/section[2]/div/section[2]/form/div/main/div[2]/div/div"
                    ).text
                    website_name = browser.find_element_by_xpath(
                                "/html/body/div[3]/div/div[2]/div/section[2]/div/section[2]/form/header/div[1]/h3"
                                ).text
                if website_name == '':
                    website_name = placements_checklist[:placements_checklist.find(' ')]
                num = placements_checklist[placements_checklist.find('(') + 1:placements_checklist.find('/') - 1]
                den = placements_checklist[placements_checklist.find('/') + 2:placements_checklist.find(')')]
                if num != den or placements_checklist.text == 'Nothing found':
                    click_everything(browser, website_name)
        except:
            if i > amount_of_websites:
                print(final)
                break
            else:
                time.sleep(10)
                i -= 1



def click_everything(browser, website):
    print(website)
    try:
        browser.find_element_by_xpath(
            "/html/body/div[3]/div/div[2]/div/section[2]/div/section[2]/form/div/main/div[1]/div[2]/div/input").send_keys(website)
    except:
        browser.find_element_by_class_name("input").send_keys(website)
    print("and the law won")
    time.sleep(10)
    for x in range(15):
       try:
           browser.find_element_by_xpath(
               "/html/body/div[3]/div/div[2]/div/section[2]/div/section[2]/form/div/main/div[1]/div[1]/button[2]").click()
           break
       except:
           print("ae!")
           time.sleep(1)
    for x in range(15):
        try:
            print("tentando o primeiro")
            browser.find_element_by_xpath(
                  "/html/body/div[3]/div/div[2]/div/section[2]/div/section[2]/form/div/main/div[2]/div/div/div/div[1]/div[1]/div"
            ).click()
            #browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/section[2]/div/section[2]/form/div/main/div[2]/div/div/div/div[1]/div[1]/div").click()
            break
        except:
            time.sleep(1)
    browser.find_element_by_xpath(
            "/html/body/div[3]/div/div[2]/div/section[2]/div/section[2]/form/header/div[2]/button"
            ).click()


def calculate_total_amount_of_websites(browser):
    time.sleep(10)
    for i in range(500, 2000):
        try:
            browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/section[2]/div/section[1]/div/div/table/tbody/tr[' + str(i) + ']/td[1]')
        except:
            break
    return int(i)


#websites = ['conmishijos.com', 'freescores.com']
websites_formatted = []
websites_formatted.extend([result[:18] + '...' if len(result) > 18 else result for result in websites])
browser = login_adform()
time.sleep(5)
browser = select_inventory(browser)
time.sleep(5)
amount_of_websites = calculate_total_amount_of_websites(browser)
print(amount_of_websites)
print(type(amount_of_websites))
select_website_name(browser, websites_formatted, amount_of_websites)

