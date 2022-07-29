
from selenium import webdriver

gecko_driver_path = 'C:\Development\geckodriver'

driver = webdriver.Firefox(executable_path=gecko_driver_path)

# driver.get('https://www.amazon.com/Rechargeable-Windproof-Flameless-Indicator-Cigarette/dp/B07L61G21Q/ref=sr_1_2?keywords=lighters+for+smoking&qid=1643220989&sprefix=lighter%2Caps%2C677&sr=8-2')


# price = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[9]/div[3]/div[4]/div[11]/div[1]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]')    #id("price_inside_buybox")
# print(price.text)
# driver.get('https://www.python.org/')
# dates = driver.find_elements_by_css_selector('.event-widget .shrubbery ul li time')
# date_list = [str(item.text) for item in dates]
# titles = driver.find_elements_by_css_selector('.event-widget .shrubbery ul li a')
# title_list = [str(itm.text) for itm in titles]
# events = {}
# for i in range(0,len(title_list)):
#     events[i]={
#         'time':date_list[i],
#         'name':title_list[i]
#     }
# print(events)






# driver.close()
driver.quit()
