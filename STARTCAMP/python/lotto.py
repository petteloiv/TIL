# 1 ~ 45 중에 6개만 뽑아서 리스트에 담아서 출력 

import random 

#winners에 변수 직접 입력 대신 lotto_api.py의 코드 사용하면 된다.
winners = [4,7,14,16,24,44]

 #리스트로 만들어준다. 더 깔끔..! 
numbers = list(range(1,46)) 

#비복원추출로 6개 뽑기
#6개 뽑아서 lotto 변수에 담기를 1000번 반복

for i in range(1000) :
    lotto = random.sample(numbers, 6) 
    # 당첨횟수를 기록 = 0 count 초기화
    count = 0
    # print(lotto[0]~[5]) 로또에 들어있는 각 숫자 
    for num in lotto:   
        # print(num)
        # lotto가 가지고 있는 값들 하나하나가
        # winners 안에 들어 있다면,
        if num in winners:
            count = count + 1 
        # 한 개 당첨
    # 6개 당첨 == 1등 
    if count == 6:
        print(i)
        print('1등!!!!!')



# 혼자 해 볼 때 자꾸 새 변수에 random으로 뽑은 값을 저장하는거 까먹음.. 주의 
# range() 0부터 시작하니까 시작 숫자 바꾸고 싶으면 range(시작점, n)

