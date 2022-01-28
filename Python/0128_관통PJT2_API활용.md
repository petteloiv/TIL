## 관통프로젝트 - 파이썬을 활용한 데이터수집 2 

- Python 기초 문법 실습
- 데이터 구조에 대한 분석과 이해 
- 요청과 응답에 대한 이해
- API의 활용과 문서 분석 



### 외부 데이터를 수집하여 원하는 결과를 도출하기 

- 인기 영화 조회
- 특정 조건에 맞는 인기영화 조회 - 평점 8점 이상
- 특정 조건에 맞는 인기영화 조회 - 평점 순 정렬
- 특정 영화 추천 영화 조회
- 특정 영화 배우, 감독 리스트 조회 



### 1. 웹 스크래핑

- 주소(url)통해 요청 보내고,, 결과로 문서  받아온다 

#### requests 

- 파이썬 위한 요청-응답 받을 수 있는 라이브러리 

```bash
$ pip install requests
```

#### BeautifulSoup

- HTML / XML 파일에 있는 데이터를 뽑아주는 라이브러리 

```bash
$ pip install beautifulsoup4
```



#### 정보스크랩 단계

1. 주소로 요청 보내기 

```python
# 1. 정보가 있는 사이트 url을 준비 

url = 'https://www.naver.com/'

# 2. 요청 보내기 / 결과 변수에 저장 ..! 

import requests 
response = requests.get(url)

print(response, type(response)) # 출력해서 확인
# response (200) <= 성공적으로 정보 가져왔다는..약속

# 3. 원하는 속성으로 변환.. 

response = requests.get(url).text #문자열 됐어요 
print(response)
```

2. 파싱 및 활용 

```python
# BeautifulSoup으로 (text -> 다른 객체 변환)

from bs4 import BeautifulSoup # 이거 맨 윗줄

# 변수에 저장.. 
# HTML 파일에 있는 데이터 가져오기 위해서 활용
data = BeautifulSoup(response, 'html.parser')
# print(type(data)) beautifulsoup 어쩌고로 바뀐거 확인

# 내가 원하는 정보 찾기
kospi = data.select_one('선택자')
# print(kospi.text) # 텍스트만 뽑아서 보여줌 ..

```



#### 선택자 (다음주 수업)

- HTML에서 쓰이는 기준.. 같은거
- 화면에서 우클릭 > 검사 누르면 ... 선택자 뜬다 copy > copy selector 



#### JSON()

- 데이터 주고받을 때 자주 사용! 
- json viewr 이용하면 편하다 .. 



### 2. API (Application Programming Interface)

- 컴퓨터나 컴퓨터 프로그램 사이의 연결
- 일종의 소프트웨어 인터페이스이며 다른 종류의 소프트웨어에 서비스를 제공
- 사용하는 방법을 기술하는 문서나 표준은 API 사양/명세 (specification)

---

- 어떤 정보들을 확인해야할까?
  - 주소(Url), 문서(JSON)

- API == 실시간 데이터 받고싶으면 ,,,
- 파일 데이터 == 과거 데이터  

#### API 활용하는 법 

- 요청하는 방식에 대한 이해
  - 인증 방식
  - URL 생성
    - 기본 주소
    - 원하느 ㄴ기능에 대한 추가 경로
    - 요청 변수 (필수와 선택)
- 응답 결과에 대한 이해
  - 응답 결과 타입 (JSON)
  - 응답 결과 구조



#### API 명세 예시 (네이버 영화)

1. 인증 방식
2. API 기본 정보
   - 출력 포맷에 맞는 주소로 요청 보내기 
3. 요청 변수 
   - 요청 변수명, 타입
4. 출력 결과
   - 어떤 값을 어떤 타입으로 주겠다! 설명되어있음



#### API 명세 예시 (공공데이터 포털)

1. 요청 주소
2.  요청 변수 
3. 출력 결과 