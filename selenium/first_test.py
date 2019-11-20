from selenium import webdriver

chromedriver = ("/Users/vikramsinghal/Documents/python_project/automate_browser/chromedriver")
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.wikipedia.com")