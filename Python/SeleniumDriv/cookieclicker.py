from selenium import webdriver
import time
gecko_driver_path = 'C:\Development\geckodriver'

driver = webdriver.Firefox(executable_path=gecko_driver_path)

driver.get('https://orteil.dashnet.org/experiments/cookie/')
check = time.time()+5
time_out = time.time()+(60*5)

cookie = driver.find_element_by_xpath('//*[@id="cookie"]')
while True:
    cookie.click()
    if time.time()>=check:
        price=[]
        money = int(driver.find_element_by_id('money').text)
        store = driver.find_elements_by_css_selector('#store b')
        prices = [int(item.text.split('-')[1].replace(',','')) for item in store if len(item.text)>0]
        price=[itm for itm in prices if money>itm]
        if len(price)>0:
            thing = max(price)
            index = prices.index(thing)
            store[index].click()
        check=time.time()+5
    if time.time()>=time_out:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break

driver.quit()