# 1. requests 불러오기
# 2. 나이 예측 api 사용
# 3. 특정 이름을 입력 했을 때, 무작위 나이를 가져와서
# ~~의 나이는 ~~살입니다. 라는 문자를 출력 

# 풀었지만 틀림 - f string 제대로 사용 못함.. 

# import requests

# url = 'https://api.agify.io/?name=elly'
# response = requests.get(url).json()

# name = response['name']
# age = response['age']

# print("{0}의 나이는 {1}살입니다.".format(name,age))

# ------------------------------------------------

import requests

name = input('이름을 입력해 주세요 : ')
url = f'https://api.agify.io/?name={name}'

response = requests.get(url).json()

age = response['age']
print(f'{name}의 나이는 {age}살 입니다.')