# 챗봇 / api 복습
# 부산의 날씨 알아보기 

import requests

name = input('도시의 이름을 영어로 입력해주세요 : ')


url = f'https://www.metaweather.com/api/location/search/?query={name}'
response = requests.get(url).json()

woeid = int(response["woeid"])

url2 = f'https://www.metaweather.com/api/location/{woeid}'
response2 = requests.get(url2).json()

weather = str(response["weather_state_name"])

print(f"{name}의 날씨는 {weather}입니다.")