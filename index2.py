from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://www.naver.com/') as response:
# 원하는 사이트의 주소를 입력
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.select("strong.title"):
    # .select를 이용하여 strong 태그의 title class를 얻기
        print(anchor)
        # 지금 얻으려는 정보들은 .get을 할 이유가 없기에 삭제

from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://www.naver.com/') as response:
    soup = BeautifulSoup(response, 'html.parser')
    f = open("ex.txt", 'w')
    # f라는 변수에 쓰기 전용으로 ex.txt파일 생성
    for anchor in soup.select("strong.title"):
        data = anchor.get_text() + "\n"
        # 원하는 정보의 text만 추출 + 줄바꿈
        f.write(data)
        # f라는 변수에 data를 쓰기
    f.close()
    # f 변수(ex.txt) 닫기
