## 고지식한 알고리즘 (Brute Force)



### Brute Force 개념

- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서패턴 내의 문자들을 일일히 비교하는 방식으로 동작 

- 고지식한 패턴 검색 알고리즘의 시간 복잡도 
  - 최악의 경우 텍스트의 모든 위치에서 패턴 비교해야해서 O(MN)



### 교수님 예시 



![image-20220216110240585](C:\Users\petteloiv\AppData\Roaming\Typora\typora-user-images\image-20220216110240585.png)



```python
수도코드 

for i : 0 -> N - M :
        for j : 0 -> M -1 
            t[i+j] == p[j] ... ?
            
        j == M (패턴 끝까지 돌았으면 성공)

```

```
인덱스 0으로 놓고 비교
값이 같으면 둘 다 증가하며 다음것 비교! 

값 다르면 ... 
i => 다음 시작점으로 이동 (시작 인덱스 +1)
j => 원점.. (시작 인덱스 0)
```

```python
def BruteForce (p,t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스 
    while j < M and i < N:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i + 1
        j = j + 1 
    if j == M : return i - M # 검색 성공
    else : return -1 # 검색 실패 
```

```
# 0216 string 오전 라이브 강의에 해설 있음
이해.. 잘 ... 못해서 다시 들을 것! 
```

