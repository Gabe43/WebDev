from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

gecko_driver_path = 'C:\Development\geckodriver'

driver = webdriver.Firefox(executable_path=gecko_driver_path)

driver.get('http://secure-retreat-92358.herokuapp.com/')
# value = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]')
# print(value.click())


# input = driver.find_element_by_name('search')
# input.send_keys('Python')
# input.send_keys(Keys.ENTER)
elements = driver.find_elements_by_css_selector('.form-signin input')
details = ['Saptarshi','Nag','nagsaptarshi03@gmail.com']

for item in range(0,len(details)):
    elements[item].send_keys(details[item])

clck = driver.find_element_by_tag_name('button')
clck.click()

# driver.quit()
