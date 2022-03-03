## Django 기초 2 



### 1. HTML Form 

- HTML Form element
  - 웹에서 사용자 정보를 입력하는 여러 방식 제공하고, 사용자로부터 할당된 데이터를 서버로 전송 (정해져있는 위치로) 하는 역할 담당
  - 핵심 속성
    - action : 입력 데이터가 전송된 url
    - method : 입력 데이터 전달 방식 지정 
  
- HTML input element
  - 사용자로부터 데이터를 입력 받기 위해 사용
  - type 속성에 따라 동작 방식이 달라짐
  - 핵심 속성
    - name 
    - name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있음
    - 주요 용도 ; GET/POST 방식 => 서버에 전달하는 파라미터로 매핑
    -  GET 방식 : url에서 ?key=value&key=value 형식으로 데이터 전달 

- HTML label element 
  - 사용자 인터페이스 항목에 대한 설명 나타냄
  - 인풋이랑 그냥 한 세트라고 생각하기!
  - label을 input 요소와 연결하기
    - input 에 id 속성 부여
    - label에는 input의 id와 동일한 값의 for 속성이 필요

- for 속성
  - for 속성 값과 일치하는 id를 가진 문서의 첫번째 요소 제어
  
- id 속성
  - 전체 문서에서 고유해야하는 식별자 정의 
  - 많은 요소들에 적용하려면 class 사용하기 
  
  