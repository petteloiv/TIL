import requests
import json

headers = {'Accept': 'application/json','Content-Type': 'application/json; chearset=utf-8'}
data = {'nickname': '부울경2반박지현', 'yourAnswer': 'Kubernetes'}

res = requests.post('http://13.125.222.176/quiz/jordan', data=json.dumps(data), headers=headers)
print(str(res.status_code) + " | " + res.text)