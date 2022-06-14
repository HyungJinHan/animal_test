from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

elem = driver.find_element(By.NAME, "q")

elem.send_keys("adidas")

elem.send_keys(Keys.RETURN)

# assert "Python" in driver.title
# elem.clear()
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
