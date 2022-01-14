# 1. requests 불러오기
import requests

# 2. requests 사용해서 로또 api에 데이터 요청 (조회요청)
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=997'
response = requests.get(url).json()

# 3. 요청 보내서 응답 받은 문서를 출력 (로또 당첨 번호 출력)
# print(response)
# print(response['drwtNo1'])
# print(response['drwtNo2'])
# print(response['drwtNo3'])
# print(response['drwtNo4'])
# print(response['drwtNo5'])
# print(response['drwtNo6'])

# 5. List에 당첨 번호 정보 담기

winners = [] 


# 4. 좀 더 스마트하게 코드 변경
# 문자열+숫자 일 때 f string 사용 

for num in range(1,7):
    print(response[f'drwtNo{num}'])
    #winners 리스트에 당첨번호 추가
    winners.append(response[f'drwtNo{num}'])
print(winners)

