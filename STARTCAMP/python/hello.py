# 변수 라는 개념  
dust = 60 # dust가 변수 

greeting = "Hello, World!"

print(greeting) # print() 출력하게 하는 함수

# 터미널에서 명령어 사용해 파일 실행 시킨다
# $ python hello.py <- $ python 파일명

# 여러번 출력하고 싶으면 여러번 붙여넣으면 된다 (줄바꿈 필수)

# ctrl + / == 내가 지정한 영역 주석처리
# print(greeting)
# print(greeting)
# print(greeting)
# print(greeting)

# while 사용해 4번 출력 

count = 0 #종료조건 위한 변수..
while count < 4 :
    # 조건을 만족하는 동안 아래 코드 실행
    print(greeting)
    count = count + 1  # 종료조건 위해 count 숫자 변경시켜준다
print('while문 끝남')

# for 사용해 4번 출력
# 정해진 범위 안에서 반복 실행
# 범위는 ... 어디서 구하지?
# range(n) == 0 ~ n-1 숫자... 
for i in range(4):
    print(greeting)
print('for문 끝남')
