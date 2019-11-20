from selenium import webdriver
from selenium import by
chromedriver = "/Users/vikramsinghal/Documents/GitHub/Projects/automate_browser/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.wikipedia.com")
print ("Current website you are viewing is " + driver.current_url)
print ("Title of the website is " + driver.title)
print ("Driver you are using is " + driver.name)
enter = driver.find_element_by_id("searchInput")
find_element_by_id.send_keys("Automation")
