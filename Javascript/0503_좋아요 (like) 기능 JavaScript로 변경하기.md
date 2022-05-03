## 좋아요 (like) 기능 JavaScript로 변경하기 



- 기존
  - django에서 post 요청 보내서 views.py에서 처리
  - 클릭 일어날 때마다 redirect돼서 새로고침이 일어남 
- 수정할 부분
  - html -> js 코드 (`<script>` 추가)
  - views.py -> 데이터 Json으로 가공해서 보내는 함수로 수정 필요



#### 1. html 수정

- url, action, method 모두 사용 X => 삭제해주자!

- script에서는 DTL 사용이 불가능! 

  - 구체적인 폼 태그 등 선택과 변하는 pk값 사용을 위해 속성 추가 필요

  - ```javascript
    <form class="like-form" data-article-id="{{ article.pk }}" >
    ```

  - `<span>` 태그 붙여야하는 친구들 붙여주기

    - span으로 감싸면 css나 js로 그 부분 변형이 가능



#### 2. script 구조 생각하기

- 얘를 통해서 할 행동을 먼저 정의하고 코드 짜기
- 버튼 클릭 통해 like가 변화하면 "좋아요 / 좋아요 취소" 와 좋아요 누른 인원수 변경해서 **새로고침 없이** 화면에 나타내기
- 필요한 정보 ; 좋아요 여부 / 좋아요 누른 사람의 수 => views.py에서 처리, json으로 정보 받아와서 처리하기 



#### 3. views.py 작성 

- 로그인 되어 있을 ㄸㅒ만 (조건)  => 로그인 안되어있으면 로그인 페이지로!
- 특정 글 받아오기 `get_object_or_404`
- 게시글과 현재 유저가 MTM 관계 맺고 있는지 확인!!!
  - filter로 데이터 안에 user가 있는지 확인
    - 있으면 좋아요 취소 / 없으면 좋아요 눌러주기
    - liked 옵션 추가해서 False, True 넣어주기 (json에 넣을 값)
  - context에 liked 여부, count 값 넣어서 JsonResponse로 리턴 



#### 4. script 작성

- 행동 일어나는 부분 querySelector로 잡아오기

  - form 태그 (이 경우에는 form태그 전부 받아와야해서 All)
  - csrf (얘는 모든 값이 같아서 하나만 받아오면 됨!) => 얘는 그 안에 담겨있는 value 받아오기

- forms 중 하나의 form에 해당하는 행동 할 테니까 forEach 사용하기

- eventListener 추가 => 'submit' / event.preventDefault 처리해주기

- event 일어나면 axios로 요청 보내자

  - axios 필요 정보 ; url, method, headers(csrf)

- .then (정보 성공적으로 받아왔을 때)

  - ```javascript
    const { liked, count } = response.data
    ```

  - 데이터 받아와서 사용하기

  - btn과 count 정보 변경

    - 어쩌구저쩌구.innerText = '보여주고 싶은 값!'

- .catch (실패 -> 에러났을 때)

  - 에러 일어나면 특정 위치로 보내버리자!
    - 상대 경로로 작성 가능하다

