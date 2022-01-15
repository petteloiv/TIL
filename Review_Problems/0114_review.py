# 챗봇 / api 복습
# 부산의 날씨 알아보기 

import requests

name = input('도시의 이름을 영어로 입력해주세요 : ')


url = f'https://www.metaweather.com/api/location/search/?query={name}'
response = requests.get(url).json()

woeid = response[0]['woeid'] #api의 리스트 안의 딕셔너리의 요소... 키값 

url2 = f'https://www.metaweather.com/api/location/{woeid}'
response2 = requests.get(url2).json()

consolidated = list((response2.keys())[0]['weather_state_name'])
weather = consolidated[1]['weather_state_name']

print(f"{name}의 날씨는 {weather}입니다.")