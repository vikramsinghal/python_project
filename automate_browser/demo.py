import time
from selenium import webdriver
chromedriver = "/Users/vikramsinghal/Documents/python_project/automate_browser/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.wikipedia.com")
print ("Current website you are viewing is " + driver.current_url)
print ("Title of the website is " + driver.title)
print ("Driver you are using is " + driver.name)
enter = driver.find_element_by_id("searchInput")
element.send_keys("Automation")
time.sleep(2)

# driver.quit()
