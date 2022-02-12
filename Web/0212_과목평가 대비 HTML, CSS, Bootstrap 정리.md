##  과목평가 대비 HTML, CSS, Bootstrap 정리 :muscle:

[TOC]



## HTML

### 1. About HTML 

- HTML 
  - Hyper Text Markup Language
  - 웹 페이지를 작성(구조화)하기 위한 언어
  - 웹 페이지가 어떻게 구조화되어 있는지 알 수 있도록 하는 마크업 언어
- 웹표준 만드는 곳 : W3C (협회), WHATWG (기업들)



### 2. HTML 기본 구조

- html : 문서의 최상위 요소 (root)
- head : 문서 메타데이터 요소
  - 일반적으로 브라우저에 나타나지 않음!
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등 
- body  : 문서 본문 요소
  - 실제 화면 구성과 관련된 내용 

---

#### 2-1. DOM 트리

- Document Object Model 
- 텍스트 파일인 HTML 문서를 브라우저에서 **렌더링** 하기 위한 구조 

- 기능
  1. HTML 문서에 대한 모델 구성
  2. HTML 문서 내의  각 요소에 접근 / 수정에 필요한 프로퍼티, 메서드 제공 

---

#### 2-2. 요소 (element)

- HTML의 요소 => 태그 + 내용 (contents)
- 태그는 내용(컨텐츠) 감싸는 것으로 정보의 성격과 의미 정의
- 내용 없는 태그들 있음! (닫는 태그 없음)
  - br, hr, img, input, link, meta
- 요소는 중첩(nested) 가능! 
  - 여는 태그 - 닫는 태그 쌍 잘 확인해야함!
    - 오류 XX 레이아웃 깨져서 출력 => 디버깅 힘들다

---

#### 2-3. 속성 (attribute)

- 태그 안에 입력해 태그의 부가적 정보 설정
- 태그별로 사용할 수 있는 속성 다르다.
- 이름 - 값이 하나의 쌍으로 존재! 
  - `속성명="값"`

- HTML Global Attribute
  - 모든 HTML 요소가 공통으로 사용할 수 있는 속성!
    - `id` 
    - `class`
    - `style` : inline 스타일
    - `data-*` : 페이지에 개인 사용자 정의 데이터 저장
    - `title` : 요소 대한 추가 정보
    - `tabindex` : 탭 순서

---

#### 2-4. 시맨틱 태그 !!!!!

- 등장 : HTML5
- 의미론적 요소 담은 태그로, 기존 영역을 의미하는 div 태그 대체하여 사용
- 대표적인 태그
  - `<header>`: 문서 전체나 섹션의 머리말 부분
  - `<nav>` : 내비게이션
  - `<aside>` : 사이드에 위치한 공간, 메인 콘텐츠와 관련성 적은것
  - `<section>` : 문서의 일반적 구분, 컨텐츠 그룹
  - `<article>` : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - `<footer>` : 문서 전체나 섹션의 푸터(마지막 부분)
  - `+` `<h1>` `<table>` 태그들도 시맨틱 태그로 볼 수 있다! 
- 장점
  - 요소의 의미가 명확해져 코드의 가독성 상승
  - 유지보수가 쉬워짐
  - 효과적으로 활용하면 검색엔진최적화(SEO)에 도움

---

#### 2-5. head

##### 1. 구성요소 

- `<title>` : 브라우저 상단 타이틀
- `<meta>` : 메타데이터 요소
- `<link>` : 외부 리소스 연결 요소 (CSS, favicon ...)
- `<script>` : 스크립트 요소 (JS파일,..)
- `<style>` : CSS 직접 작성 

##### 2. Open Graph Protocol

- 메타 데이터를 표현하는 새로운 규약
  - HTML 문서의 메타 데이터 통해 문서 정보 전달
  - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의
  - og : 로 작성! 
  - 링크만 보내도 메타데이터 보여주는 기능 (카톡 미리보기!)



### 3. HTML 문서 구조화

#### 3-1. 인라인 / 블록 요소

---

#### 3-2. 텍스트 요소

---

#### 3-3. 그룹 컨텐츠

---





## CSS

### 1. About CSS 

- CSS
  - Cascading Style Sheets
  - 사용자에게 문서(HTML)를 표시하는 방법을 지정하는 언어
  - 스타일을 지정하기 위한 언어
  - 선택 후 스타일 지정 

---

#### 1-1. CSS 구문

- 선택자 (Selector) 
  - 스타일을 지정할 HTML 요소 선택 
- 선언(Declaration)
  - 중괄호 안에서 속성과 값 (하나의 쌍)으로 이루어진 선언 진행
- 속성(Property)
  - 요소의 속성  : 어떤 스타일 기능 변경할지 결정
- 값(Value)
  - 속성에 부여할 값 : 어떻게 스타일 기능 변경할지 결정 

![image-20220212215045789](과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220212215045789.png)

---

#### 1-2. CSS 정의 방법

- 인라인 (inline)
  - 해당 태그에 직접  style 속성 활용
- 내부 참조(embedding) - `<style>`
  - `<head>` 안에 `<style>` 태그 만들어 지정 
- 외부 참조(link file) - 분리된 CSS 파일
  - 외부 CSS 파일을 `<head>` 내 `<link>` 통해 불러오기 



### 2. CSS 선택자

#### 2-1. 선택자 유형

1. 기본 선택자
   - 전체 선택자, 요소 선택자
   - 클래스 선택자, 아이디 선택자, 속성 선택자
2. 결합자 (Combinators)
   - 자손 결합자, 자식 결합자
   - 일반 형제 결합자, 인접 형제 결합자
3. 의사 클래스/요소 (Pseudo Class)
   - 링크, 동적 의사 클래스
   - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

---

#### 2-2. CSS 선택자 정리 

- 요소 선택자
  - HTML 태그를 직접 선택
- 클래스(class) 선택자
  - 마침표(`.`) 로 시작
  - 해당 클래스가 적용된 항목 선택
- 아이디(id) 선택자
  - `#` 문자로 시작
  - 해당 아이디가 적용된 항목 선택
  - 단일 id 사용 !!! 

---

#### 2-3. css 결합자 정리

- 자손 결합자
  - selector A 하위의 모든 selector B 요소
- 자식 결합자
  - selector A 바로 아래의 selector B 요소
- 일반 형제 결합자
  - selector A의 형제 요소 중 뒤에 위치하는  selector B 요소 모두 선택 

- 인접 형제 결합자
  - selector A의 형제 요소 중 바로 뒤에 위치하는  selector B 요소 선택 (하나) 

---

#### 2-4. CSS 적용 우선순위 (cascading order)

1. 중요도(Importance) => 사용시 주의 
   - `!important` 
2. 우선 순위 (Specificity)
   -  인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
3. CSS 파일 로딩 순서 

---

#### 2-5. CSS 상속

- 상속을 통해 부모 요소의 속성을 자식에게 상속한다. 
  - 상속 되는 것과 안되는 것 있다!!!! 
- 상속 되는 것 
  - Text 관련 요소
    - font, color, text-align
  - opacity
  - visibility
- 상속 되지 않는 것 
  - Box model 관련 요소
    - width, height, margin, padding, border, box-sizing, display 
    - 그래서 d-flex도 상속 안된다... 
  - position 관련 요소
    - position, top/right/bottom/left, z-index 



### 3. CSS 기본 스타일 

#### 3-1. 크기 단위 

- `px` (픽셀)
  - 모니터 해상도의 한 화소인 '픽셀' 기준
  - 픽셀 크기 변하지 않음 (고정적 단위)
- `%` 
  - 백분율 단위
  - 가변적 레이아수에서 자주 사용
- `em`
  - (바로 위, 부모 요소에 대한) 상속 영향 받음
  - 배수 단위, 요소에 지정된 사이즈에 상대적 사이즈 가짐
- `rem` 
  - 부모 요소 대한 상속 영향 XXXX 받지 않음! 
  - 최상위 요소 (html) 사이즈 기준으로 배수 단위 가짐
- `viewport`
  - 웹페이지 방문한 유저에게 바로 보이게 되는 웹 컨텐츠 영역
  - 디바이스 viewport 기준으로 상대적 사이즈 결정
  - `vw`, `vh`, `vmin`, `vmax` 

---

#### 3-2. 색상 단위

- 색상 키워드 
  - 대소문자 구분 X 
  - red, blue, black 등 특정 색을 직접 글자로 나타냄
- RGB 색상
  - 16진수 / 함수형 표기법 사용해 표현
  - #ff0000 
  - rgb(0, 0, 0)
  - `+` rgba (a == alpha 투명도) : rgba(0, 0, 0, 0.5)
- HSL 색상
  - 색상, 채도, 명도 통해 특정 색 표현
  - hsl(120, 100%, 0)
  - `+` rgba (a == alpha 투명도) : hsla(120, 100%, 0.5)



### 4. Box model 박스모델 

- 모든 HTML 요소는 box 형태로 되어있음
- 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.
- 하나의 박스는 네 부분으로 이루어진다.
  - content
  - padding
  - border
  - margin

![image-20220212224424381](과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220212224424381-16446734658711.png)

#### 4-1. Margin 

- top, right, bottom, left (상하좌우)
- shorthand 

---

#### 4-2. padding

- top, right, bottom, left (상하좌우)
- shorthand

---

#### 4-3. border

- 테두리...

- top, right, bottom, left (상하좌우)에 width, style, color 줄 수 있다 

- shorthand

  - ```css
    .border{
        border: 2px dashed black;     
    }
    ```

---

#### 4-4. box-sizing 

- 기본적으로 모든 요소의 box-sizing은 content-box
  - padding 제외한 순수 contents 영역만을 box로 지정
- box-sizing을 **border-box** 로 설정
  - 



### 5. CSS Display

#### 5-1. display : block 

- 줄 바꿈이 일어나는 요소
- 화면 크기 전체의 가로 폭 차지
  - 가질 수 있는 너비의 100%
  - 가로 꽉꽉 채워서 가져간다
- 블록 요소 안에 인라인 요소 들어갈 수 있다!
- 대표 block  요소 
  - 

---

#### 5-2. display: inline

-  줄 바꿈 일어나지 않는 행의 일부 요소
- content 너비만큼만 가로 폭 차지
- width, height, margin-top, margin-bottom 지정 불가 ㅠㅠ 
- 상하 여백 : line-height로 지정
- 대표 inline 요소 
  - 

---

#### 5-3. display : inline-block

- block과 inline 레벨 요소의 특징 모두 가짐
- inline 처럼 한 줄에 표시 가능! 
- block 처럼 width, height, margin 속성 모두 지정 가능

---

#### 5-4. display: none

- 해당 요소 화면에 표시 X 공간 부여 X 
- 근데 그러면 왜 쓰는지 모르겠다 .. 



### 6. CSS Position

- 문서 상에서 요소 위치를 지정할 때 사용
- position으로 위치 기준 변경

- static : 모든 태그의 기본 값 (기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소 위치 기준으로 배치

#### 6-1. relative 상대위치 

- 자기 자신의 static 위치 기준으로 이동
- 레이아웃에서 요소가 차지하는 공간은 static 일 때와 같음
- normal flow 유지

---

#### 6-2. absolute 절대위치

- 요소를 일반적인 문서 흐름에서 제거 (레이아웃에 공간 차지 X)
- 가장 가까이 있는 부모/조상 요소 기준으로 이동
  - 없는 경우 body 따라간다
- normal flow에서 벗어남! 

---

#### 6-3. fixed 고정위치

- 요소를 일반적인 문서 흐름에서 제거 (레이아웃에 공간 차지 X)
- 부모 요소와 관계 X viewport 기준으로 이동 
  - 스크롤 시 항상 같은 곳에 위치
- normal flow에서 벗어남! 



### 7. Flexbox 

- 2012년에 개발됨
- 장점
  - 수동 값 부여 없이 수직 정렬
  - 수동 값 부여 없이 아이템의 너비와 높이, 간격을 동일하게 배치 가능
- 행과 열 형태로 아이템 배치하는 1차원 레이아웃 모델 

![image-20220212231126574](과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220212231126574.png)

- 축
  - main axis (메인 축)
  - cross axis (교차 축)
- 구성 요소
  - flex container (부모 요소)
  - flex item (자식 요소)

---

#### 7-1. Flexbox 구성 요소

- Flex Container (부모 요소)
  - flexbox 레이아웃 형성하는 가장 기본적인 모델
  - flex item들이 놓여있는 영역
  - display 속성 flex 혹은 inline-flex로 지정
    - bootstrap d-flex가 이것 .. 
- flex item (자식요소)
  - 컨테이너에 속해 있는 컨텐츠 (박스)

---



### 8. Grid

- 2017년에 개발 