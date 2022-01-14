# import시 주의할 점
# import 가지고 오는 행위
# 이 이후로 활용할 코드를 가지고 올 것이기 때문에
#  import는 항상 최상단에 작성한다.

# import module은 코드 쓰다가 필요할 때 불러오기
import random

menu = ['샐러드', '서브웨이', '파스타'] 

choice = random.choice(menu)

print(choice)

# 파이썬 문법 convention 있다.. 
# 코드 실행에는 문제가 없지만 가독성을 위한 것



