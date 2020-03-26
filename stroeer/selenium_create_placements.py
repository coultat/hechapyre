from create_placements_stroeer_ssp import transforming_placements_json, transforming_websites_json, merging_placements_websites
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from store.sample import placements
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from store.login import login
import time

def get_json_data():
    websites_json = []
    placements_json = []
    final_json = []
    placements.sort()
    placements_json = transforming_placements_json(placements)
    websites_json = transforming_websites_json(placements)
    websites_json = merging_placements_websites(websites_json, placements_json)
    return websites_json


def login_stroeer():
    driver = webdriver.Firefox()
    driver.get(login.stroeer_url)
    time.sleep(7)
    driver.find_element_by_name('email').send_keys(login.stroeer_login)
    driver.find_element_by_name('password').send_keys(login.stroeer_pw)
    driver.find_element_by_class_name('auth0-label-submit').click()
    return driver


def checking_websites(driver, website, helper):
    if website[helper[2]] != 'yes':
        driver = writing_the_website(driver, website['website'] + helper[1])
        website[helper[2]] = finding_the_name(driver, website['website'] + helper[1])
        delete_field_name(driver)


def delete_field_name(driver):
    time.sleep(0.25)
    driver.find_element_by_xpath(
        '/html/body/pm-root/div/ng-component/div/div/pm-portfolio-master-overview/div[1]/ibb-search-bar/div/'\
        'mat-chip-list/div/mat-chip/mat-icon'
    ).click()


def writing_the_website(driver, name):
    for i in range(10000):
        try:
            driver.find_element_by_id('mat-chip-list-input-'+str(i)).send_keys(name)
            driver.find_element_by_id('mat-chip-list-input-'+str(i)).send_keys(Keys.RETURN)
            break
        except:
            pass
    return driver


def writing_website(driver, name):
    for i in range(5000):
        try:
            driver.find_element_by_xpath('//*[@id="mat-input-'+str(i)+'"]').send_keys(name + helper[1])
            driver.find_element_by_xpath('//*[@id="mat-input-'+str(i+1)+'"]').send_keys('https://' +name + '/')
            driver.find_element_by_xpath('//*[@id="mat-input-'+str(i+3)+'"]').send_keys(name + '.' +helper[0])
            break
        except:
            pass
    driver.find_element_by_xpath(
    '/html/body/pm-root/div/ng-component/div/div/pm-create-medium/div/div/form/ibb-progress-fab/button/span'
    ).click()
    time.sleep(1)
    for i in range(10):
        try:
            driver.find_element_by_xpath(
                '/html/body/pm-root/div/ng-component/div/div/pm-website-detail/div/pm-ad-slots/'\
                'ibb-no-content-info/div[3]/ibb-no-content-action-tile[1]'
                ).click()
            break
        except:
            time.sleep(0.75)


def finding_the_name(driver, name):
    time.sleep(2)
    for i in range(1,5000):
        try:
            result = driver.find_element_by_xpath(
                '/html/body/pm-root/div/ng-component/div/div/pm-portfolio-master-overview/div[1]/mat-tab-group/'\
                'div/mat-tab-body[1]/div/div/pm-media-overview/div/mat-card/mat-card-content/mat-list/'\
                'mat-list-item['+str(i)+']/div/div[3]/div[1]'
                                ).text
            if result == name:
                return 'yes'
        except NoSuchElementException:
            return 'no'
        except:
            pass


def creating_website(driver, name):
    driver.find_element_by_xpath(
                    '/html/body/pm-root/div/ng-component/div/div/pm-portfolio-master-overview/div[2]/button'
                                        ).click()
    for i in range(5000):
        try:
            driver.find_element_by_xpath('//*[@id="mat-input-'+str(i)+'"]').send_keys(name)
            driver.find_element_by_xpath('//*[@id="mat-input-'+str(i+1)+'"]').send_keys('https://' +name[:name.find('_')] + '/')
            driver.find_element_by_xpath('//*[@id="mat-input-'+str(i+3)+'"]').send_keys(name + '.' +helper[0])
            break
        except:
            pass
    driver.find_element_by_xpath(
    '/html/body/pm-root/div/ng-component/div/div/pm-create-medium/div/div/form/ibb-progress-fab/button/span'
    ).click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/pm-root/div/ng-component/div/pm-website-toolbar/header/div[1]/a/span').click()
    return driver


def checking_placements(driver, name, sizes, created):
    for i in range(20):
        try:
            driver.find_element_by_id('mat-tab-label-'+str(i)+'-1').click()
        except:
            pass
    driver = writing_the_website(driver, name)
    time.sleep(1)
    created = scrolling_placements(driver,name, created)
    delete_field_name(driver)
    return created


def scrolling_placements(driver, name, created):
    for i in range(1, 5000):
        try:
            result = driver.find_element_by_xpath(
                '/html/body/pm-root/div/ng-component/div/div/pm-portfolio-master-overview/div/mat-tab-group/div/'\
                'mat-tab-body[2]/div/div/pm-ad-slots-overview/mat-card/mat-card-content/mat-list/'\
                'mat-list-item['+str(i)+']/div/div[3]/div[2]/h4').text
            if result == name:
                created = clicking_tag(driver, i)
                break
        except NoSuchElementException:
            break
        except:
            pass
    return created


def clicking_tag(driver, i):
    platz_id = ''
    if i < 2:
        driver.find_element_by_xpath(
            '/html/body/pm-root/div/ng-component/div/div/pm-portfolio-master-overview/div/mat-tab-group/div/'\
            'mat-tab-body[2]/div/div/pm-ad-slots-overview/mat-card/mat-card-content/mat-list/mat-list-item/div/'\
            'pm-tag-generator/button'
                ).click()
    else:
        driver.find_element_by_xpath(
            '/html/body/pm-root/div/ng-component/div/div/pm-portfolio-master-overview/div/mat-tab-group/div/'\
            'mat-tab-body[2]/div/div/pm-ad-slots-overview/mat-card/mat-card-content/mat-list/'\
            'mat-list-item['+str(i)+']/div/pm-tag-generator/button'
            ).click()
    time.sleep(1)
    for j in range(30000):
        try:
            platz_id = driver.find_element_by_id('mat-input-'+str(j)).text
            break
        except:
            pass
    platz_id = platz_id[platz_id.find('d=') + 3: platz_id.find('"', platz_id.find('d=') + 3)]
    if len(platz_id) < 1:
        platz_id = ''
        time.sleep(5)
        platz_id = driver.find_element_by_id('mat-input-'+str(i)).text
        platz_id = platz_id[platz_id.find('d=') + 3: platz_id.find('"', platz_id.find('d=') + 3)]
    time.sleep(2)
    for i in range(20):
        for j in range(20):
            try:
                driver.find_element_by_xpath(
                '/html/body/div['+str(i)+']/div['+str(j)+']/div/mat-dialog-container/pm-tag-generator-dialog/div[1]/button'
                ).click()
                break
            except:
                pass
    return platz_id


def scrolling_websites_names(driver, website, name, sizes):
    time.sleep(2)
    for i in range(1,5000):
        try:
            xpath = '/html/body/pm-root/div/ng-component/div/div/pm-portfolio-master-overview/div[1]/mat-tab-group/'\
                'div/mat-tab-body[1]/div/div/pm-media-overview/div/mat-card/mat-card-content/mat-list/'\
                'mat-list-item['+str(i)+']/div/div[3]/div[1]'
            result = driver.find_element_by_xpath(xpath)
            if result.text == website:
                result.click()
                break
        except NoSuchElementException:
            break
        except:
            pass


def create_placement(driver, name, sizes):
    sizes = sizes.split(',')
    for i in range(10000):
        try:
            driver.find_element_by_id('mat-input-'+str(i)).send_keys(name)
            writing_selecting_sizes(driver, sizes, i+1)
            break
        except:
            pass
    driver.find_element_by_xpath(
        '/html/body/pm-root/div/ng-component/div/div/pm-create-banner-ad-slot/ibb-speed-dial/ibb-progress-fab/'\
        'button/span/mat-icon'
        ).click()


def writing_selecting_sizes(driver, sizes, i):
    for size in sizes:
        aux = 0
        if 'sticky' in size:
            aux = 1
            size = size.replace('sticky', '')
        driver.find_element_by_id('mat-input-'+str(i)).send_keys(size)
        try:
            driver.find_element_by_xpath('/html/body/div[2]/div/div/div/mat-option/span/span').click()
        except:
            driver.find_element_by_id('mat-input-'+str(i)).send_keys(Keys.CONTROL, "a")
            driver.find_element_by_id('mat-input-'+str(i)).send_keys(Keys.BACKSPACE)
        if aux == 1:
            driver.find_element_by_id('mat-input-'+str(i)).send_keys(size + ' sticky')
            try:
                driver.find_element_by_xpath('/html/body/div[2]/div/div/div/mat-option/span/span').click()
            except:
                driver.find_element_by_id('mat-input-'+str(i)).send_keys(Keys.CONTROL, "a")
                driver.find_element_by_id('mat-input-'+str(i)).send_keys(Keys.BACKSPACE)


def clicking_the_plus_button(driver):
    for x in range(5):
        try:
            driver.find_element_by_xpath(
                        '/html/body/pm-root/div/ng-component/div/div/pm-website-detail/div/pm-ad-slots/'\
                        'ibb-speed-dial/button'
            ).click()
            break
        except:
            time.sleep(1)
    for x in range(3):
        try:
            driver.find_element_by_xpath(
                '/html/body/pm-root/div/ng-component/div/div/pm-website-detail/div/pm-ad-slots/'\
                'ibb-speed-dial/div/button[1]'
                ).click()
            break
        except:
            time.sleep(1)


def creating_placements(driver, website, name, sizes):
    writing_the_website(driver, website)
    scrolling_websites_names(driver, website, name, sizes)
    create_placement(driver, name, sizes)
    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/pm-root/div/ng-component/div/div/pm-website-detail/div/pm-ad-slots/ibb-speed-dial/button'
                                ).click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/pm-root/div/ng-component/div/div/pm-website-detail/div/pm-ad-slots/ibb-speed-dial/div/button[1]'
                                ).click()


def create_missing_placements(driver, placements):
    final = []
    for website in placements:
        for helper in helpers:
            for placement in website[helper[0]]:
                if placement['created'] == 'no':
                    final.append([website['website']+helper[1], placement['name'], placement['sizes']])
    website = ''
    aux = 0
    for data in final:
        if website != data[0]:
            website = data[0]
            if aux > 0:
                try:
                    driver.find_element_by_xpath(
                        '/html/body/pm-root/div/ibb-cross-projects-side-navigation/ibb-side-navigation/div/div[2]/'\
                            'mat-nav-list/ibb-side-navigation-item[2]/a'
                        ).click()
                except:
                    pass
                time.sleep(10)
            writing_the_website(driver, data[0])
            aux = 1
            scrolling_websites_names(driver, data[0], data[1], data[2])
            clicking_the_plus_button(driver)
        create_placement(driver, data[1], data[2])
        clicking_the_plus_button(driver)
    driver.find_element_by_xpath(
                        '/html/body/pm-root/div/ibb-cross-projects-side-navigation/ibb-side-navigation/div/div[2]/'\
                        'mat-nav-list/ibb-side-navigation-item[2]/a'
                        ).click()


placements = get_json_data()
driver = login_stroeer()
time.sleep(10)
helpers = [['tablet', '_t', 'tab_created'],['desktop', '_d', 'desk_created'], ['mobile', '_m', 'mob_created']]
for website in placements:
    for helper in helpers:
        checking_websites(driver, website, helper)
time.sleep(5)
for website in placements:
    for helper in helpers:
        if website[helper[2]] == 'no' and len(website[helper[0]]) > 0:
            for result in website[helper[0]]:
                driver = creating_website(driver, website['website'] + helper[1])
                website[helper[2]] = 'yes'
                break
time.sleep(5)
for website in placements:
    for helper in helpers:
        for result in website[helper[0]]:
            for i in range(300):
                try:
                    driver.find_element_by_id('mat-tab-label-0-'+str(i)).click()
                    break
                except:
                    pass
            result['created'] = checking_placements(driver, result['name'], result['sizes'], result['created'])
            for i in range(300):
                try:
                    driver.find_element_by_id('mat-tab-label-'+str(i)+'-0').click()
                    break
                except:
                    pass