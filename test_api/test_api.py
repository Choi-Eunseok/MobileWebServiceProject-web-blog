import requests # 오류가 있으면 "pip install requests"
import os

HOST = 'http://127.0.0.1:8000'
res = requests.post(HOST + '/api-token-auth/', {
    'username':os.getenv("username", "username"),
    'password':os.getenv("password", "password"),
})

res.raise_for_status()
token = res.json()['token']
print(token)

# 인증이 필요한 요청에 아래의 headers를 붙임
headers = {'Authorization' : 'JWT ' + token, 'Accept' : 'application/json'}

# Post Create
data = {
    'author' : 1,
    'title' : '제목 by code',
    'text' : 'API내용 by code',
    'created_date' : '2024-06-03T18:34:00+09:00',
    'published_date' : '2024-06-03T18:34:00+09:00'
}
file = {'image' : open('./figure.jpg', 'rb')}
res = requests.post(HOST + '/api_root/Post/', data=data, files=file, headers=headers)
print(res)
print(res.json())