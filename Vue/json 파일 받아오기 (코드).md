```python
import requests
import json




file_name='popular' # 
numbers = 500
data = []
# https://api.themoviedb.org/3/movie/popular?api_key= &language=ko-KR&page=30
for i in range(1,numbers):
    url = f'https://api.themoviedb.org/3/movie/{file_name}?api_key={api_key}&language=ko-KR&page={i}'
    response = requests.get(url)
    dict_file = response.json()['results']
    for j in range(20):
        data_in = {}
        data_in['model'] = "movies.movie"
        data_in['pk'] = j+1+(i-1)*20
        
        fields_in={}
        fields_in['tmdb_id'] = dict_file[j]['id']
        fields_in['title'] = dict_file[j]['title']
        fields_in['overview'] = dict_file[j]['overview']
        fields_in['poster_path'] = dict_file[j]['poster_path']
        fields_in['adult'] = dict_file[j]['adult']
        fields_in['popularity'] = dict_file[j]['popularity']
        fields_in['vote_count'] = dict_file[j]['vote_count']
        fields_in['vote_average'] = dict_file[j]['vote_average']
        fields_in['genre_ids'] = dict_file[j]['genre_ids']
        data_in['fields']=fields_in
        data.append(data_in)
    # print(i,j)
    if i % 100 == 0:
        print(i)
    

    
with open('data.json', 'w') as fp:
    json.dump(data, fp,indent=4)
```

