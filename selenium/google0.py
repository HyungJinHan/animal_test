from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# 위의 코드는 selenium의 라이브러리를 불러오는 코드

driver = webdriver.Chrome()
# chrome을 webdriver(chromedriver.exe)로 실행는 코드를 driver라는 변수에 담기
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
# 위에서 담은 변수를 통해 파이썬 사이트를 얻는 코드 (구글 이미지로 변경)

elem = driver.find_element(By.NAME, "q")
# 개발자도구를 사용하여 검색창의 class 혹은 name등의 정보를 입력

elem.send_keys("pycon")
# 자신이 찾을 키워드를 입력하는 코드
# 키워드 입력 후 실행하면 자동으로 구글 이미지 창이 켜지며 검색창에 키워드가 입력됨

elem.send_keys(Keys.RETURN)
# 검색창에 키워드가 입력되고 엔터키를 의미하는 RETURN으로 검색 실행
# 자신이 원하는 키워드의 이미지 검색까지 완료

elem = driver.find_elements(By.CLASS, "rg_i Q4LuWd")
# 키워드에 맞는 작은 이미지를 클릭해서 다운받기 때문에 작은 이미지 class를 찾은 후 입력

# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
