# Beautiful Soup 라이브러리를 이용한 동물상 크롤링 웹 만들기
# 준비물 : Beautiful Soup 4 모듈 설치

from bs4 import BeautifulSoup
from urllib.request import urlopen
# 라이브러리 불러오는 코드 (BeautifulSoup로부터 bs4 모듈을 가져온다)

with urlopen('https://www.naver.com/') as response:
# url을 여는 라이브러리를 통해 사이트 열어서 reponse에 담기
# response = urlopen('https://www.naver.com/')와 동일
    soup = BeautifulSoup(response, 'html.parser')
    # soup라는 변수에 BeautifulSoup라는 함수를 이용해서 response를 html.parser로 분석하기
    i = 1
    # 내용 앞에 숫자 달기
    f = open("ex.txt", 'w')
    for anchor in soup.select("p.desc"):
    # 반복문을 통해 p 태그에서 class가 desc인 것을 찾기
        data = str(i) + ". " + anchor.get_text() + "\n"
        # 찾은 p 태그에서 주소를 찾아 출력하기 (.get_text()를 이용해 text만 출력)
        i = i + 1
        # 커지는 숫자를 위해 1씩 더하기
        f.write(data)
    f.close()
