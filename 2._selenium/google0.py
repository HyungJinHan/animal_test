from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# 위의 코드는 selenium의 라이브러리를 불러오는 코드
import time
# time.sleep을 위해 모듈 불러오기

import urllib.request
# 이미지 다운을 위해 모듈 불러오기

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

driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click()
# 키워드에 맞는 작은 이미지를 클릭해서 다운받기 때문에 작은 이미지 class를 찾은 후 입력
# class 검색을 위해 .rg_i.Q4LuWd으로 변경
# index 번호가 제일 첫번째인 이미지를 찾아서 클릭한다

image_s = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
# 반복문을 위해 image_s 라는 변수에 담기
[0].click()
time.sleep(3)
# 3초의 시간 지연 코드

print(driver.find_element_by_css_selector(".n3VNCb.KAlRDb").get_attribute("src"))
# n3VNCb KAlRDb 클래스의 이미지의 src 주소를 출력
imgUrl = driver.find_element_by_css_selector(".n3VNCb.KAlRDb").get_attribute("src")
# n3VNCb KAlRDb 클래스의 이미지의 src 주소를 imgUrl 이라는 변수에 담기

urllib.request.urlretrieve(imgUrl, "test.jpg")
# 위에서 얻어온 이미지의 url을 통해 imgUrl라는 변수에 담긴 이미지 다운받기

# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
