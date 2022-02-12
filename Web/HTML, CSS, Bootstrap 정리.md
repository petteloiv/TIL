## 과목평가 대비 HTML, CSS, Bootstrap 정리 :muscle:

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



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

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

**몇 가지.. 태그의 속성** 

- `<a>` 태그
  - 속성 
    -  href="URL"

```html
<a href="링크">하이퍼링크 정의하는 태그</a>
```

- <img>
  - 속성 
    - src="이미지위치"
    - width="넓이" (픽셀)
    - height="높이" (픽셀)
    - alt="이미지 설명"

```html
<img src="img_girl.jpg">
```

---

- style 속성 
  - 다른 태그들 안에 쓰임 (특정 태그 X)
    - color:red;
    - font 등..

```html
<p style="color:red;">This is a red paragraph.</p>
```

- title 속성
  - 요소 대한 추가설명
    - title="설명"

```html
<p title="I'm a tooltip">This is a paragraph.</p>
```

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
- 주의
  - 의미에 맞게 쓰도록 권장됨

```html
<!--헤더영역-->
- <header> </header> : 로고, 소개글, 메인 메뉴 등 ... (상위 요소, 다른 영역 내부에서도 사용됨)
- <h1> </h1> : 최상위 제목
- <nav> </nav> : 웹페이지의 메인 네비게이션 (보통 하나)

<!--메인-->
- <main> </main> : 이름 그대로 메인 .. 하위 영역들을 가진다
- <section> </section> : 독립적으로 떼어놓기 어려운 컨텐트 (어떤 웹페이지의 일부로만 의미 갖는 것들)
- <article> </article> : 독립적으로 분리 가능 (ex. 뉴스 사이트의 기사 각각)
- <aside> </aside> : 사라져도 지장 없는 보조 컨텐트 (ex. 사이드바, 배너)

<!--풋터-->
- <footer> </footer> : 웹사이트정보, 저작권 등의 메타데이터 주로 들어가는 부분 
```

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

##### Block 블록

- 줄 바꿈이 일어나는 요소 : 항상 새로운 줄에서 시작 .. 
- 왼쪽-오른쪽으로 꽉 차있다. full width! 
- 위, 아래 margin 가지고 있다.
- 블록 요소 안에 인라인 요소 들어갈 수 있음.

- block 요소들

  - `<article>`

  - `<div>`

  - `<footer>`

  - `<form>`

  - `<h1> - <h6>`

  - `<header>`

  - `<li>`

  - `<main>`

  - `<nav>`

  - `<p>`

  - `<section>`

  - `<ul> ` / `<ol>`

  - `<pre>`

  - `<blockquote>`

  - `<hr>`

##### inline 인라인 

- 줄 바꿈이 일어나지 않는 요소 

- content 너비만큼만 폭 차지 

- inline 요소들

  - `<a>`

  - `<b>` / `<strong>`

  - `<i> ` / `<em>`

  - `<br>`

  - `<img>`

  - `<span>`

  - `<input>`

  - `<script>`

  - `<select>`

---

#### 3-2. 텍스트 요소

![image-20220213022733564](과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220213022733564.png)

**Text formatting 요소들** (텍스트 꾸미기... )

- 사용할 단어/문장 앞뒤에 넣어서 사용 
  - 보여지는 것에 차이는 없지만 의미가 담겨있는 태그들 있다!

- `<b>` - Bold text
- `<strong>` - Bold, Important text

```html
<b>This text is bold</b>
<strong>This text is important!</strong>
```

- `<i>` - Italic text
- `<em>` - Emphasized text

```html
<i>This text is italic</i>
<em>This text is emphasized</em>
```

---

#### 3-3. 그룹 컨텐츠

![image-20220213022753355](과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220213022753355.png)

---



### 4. HTML 추가 개념들 

1. `<img>` 

   - 절대 경로
     - 깃헙 업로드하거나 폴더 위치가 변경되는 로딩되지 않는다!  
   - 상대 경로
     - 그래서 상대 경로 사용...

   ```html
   1. 절대 경로
   <img src="image/my_photo.png" alt="ssafy">
   
   2. 상대 경로
   <img src="../image/my_photo.png" alt="ssafy">
   ```

2. `<div>` 태그와 `<span>` 태그 

`<div>` 태그

-  block
-  다른 HTML 요소의 container로 사용됨
-  필수 속성은 X / style, class, id가 자주 사용됨. 
-  content block 스타일 지정에 사용됨. (CSS) 

`<span>` 태그

- **문서나 텍스트** 일부 마크업 하는데 사용되는 인라인 container! 
- 필수 속성은 X / style, class, id가 자주 사용됨. 
- 텍스트의 스타일 지정에 사용됨. (CSS)



## CSS

### 1. About CSS 

- CSS
  - **Cascading Style Sheets**
  - 사용자에게 문서(HTML)를 표시하는 방법을 지정하는 언어
  - 스타일을 지정하기 위한 언어
  - 선택 후 스타일 지정 
- 웹 브라우저는 내장된 기본 스타일이 있어 CSS 없어도 된다.
  - user agent stylesheet : 브라우저 기본 스타일 값

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

![image-20220213023422338](과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220213023422338.png)

---

#### 2-3. CSS 결합자 정리

- 자손 결합자

  - selector A 하위의 모든 selector B 요소

  ```css
  selectorA selectorB {
      
  }
  ```

- 자식 결합자

  - selector A 바로 아래의 selector B 요소

  ```css
  selectorA > selectorB {
      
  }
  ```

- 일반 형제 결합자

  - selector A의 형제 요소 중 뒤에 위치하는  selector B 요소 모두 선택 

  ```css
  selectorA ~ selectorB {
      
  }
  ```

- 인접 형제 결합자

  - selector A의 형제 요소 중 바로 뒤에 위치하는 selector B 요소 선택 (하나) 

  ```css
  selectorA + selectorB {
      
  }
  ```

---

#### 2-4. CSS 적용 우선순위 (cascading order)

1. 중요도(Importance) => 사용시 주의 
   - `!important` 
2. 우선 순위 (Specificity)
   -  인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
3. CSS 파일 로딩 순서 

```
<HW>

1. !important : 1-0-0-0-0
2. inline : 1-0-0-0
3. id 선택자 : 1-0-0
4. class 선택자 : 0-1-0
5. 요소 선택자 (p, div) : 0-0-1
6. 소스 순서 (css 파일 로딩 순서)
```

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

  - 요소에 지정된 상속된 사이즈 대해 상대적 사이즈 설정 ! 
  - (바로 위, 부모 요소에 대한) 상속 영향 받음
  - 배수 단위, 요소에 지정된 사이즈에 상대적 사이즈 가짐

  ```css
  <body style="font-size: 16px">
      <div style="font-size: 1.2em">
          hello
  	</div>
  </body>
  ```

- `rem` 

  - 부모 요소 대한 상속 영향 XXXX 받지 않음! 
  - 최상위 요소 (html) 사이즈 기준으로 배수 단위 가짐
  - root em의 약자 ... 

- `viewport`

  - 웹페이지 방문한 유저에게 바로 보이게 되는 웹 컨텐츠 영역
  - 디바이스 viewport 기준으로 상대적 사이즈 결정
  - 디바이스 상대 단위 : `vw`, `vh`, `vmin`, `vmax` 

- em, rem 

  - 공통점 
    - CSS의 font-size 속성값에 비례해 결정
  - 차이점
    - em : 부모요소 font-size 기준
    - rem: html 요소 font-size 기준

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b06bf43c-cdee-422e-9a39-1663640e64b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220212T173627Z&X-Amz-Expires=86400&X-Amz-Signature=f5b5d9a9a56872d10150372363db8222bdb3f4a285c15f5aebe3b28cd3072de3&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject" alt="img" style="zoom:80%;" />



<img src="과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220213015800428.png" alt="image-20220213015800428" style="zoom:50%;" />

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

- 테두리 바깥 여백
- 배경색의 영향을 받지 않는다! 

- top, right, bottom, left (상하좌우) 개별적으로 스타일 적용 가능 
- `margin: auto;` 로 설정하면 수평 방향 마진값 자동으로 설정
- shorthand 

```css
# 4개 속성 : top right bottom left 
margin: 10px 10px 10px 10px;

# 3개 속성 : top right&left bottom 
margin: 10px 10px 10px; 

# 2개 속성 : top&bottom right&left
margin: 10px 10px; 

# 1개 속성 : 모든 값 같게! 
margin: 10px 
```

---

#### 4-2. padding

- 내용과 테두리 사이의 간격! 
- background-color 속성으로 설정하는 배경색 영향 함께 받는다! 
- top, right, bottom, left (상하좌우) 개별적으로 스타일 적용 가능 
- shorthand

```css
# 4개 속성 : top right bottom left 
padding: 10px 10px 10px 10px;

# 3개 속성 : top right&left bottom 
padding: 10px 10px 10px; 

# 2개 속성 : top&bottom right&left
padding: 10px 10px; 

# 1개 속성 : 모든 값 같게! 
padding: 10px; 
```

---

#### 4-3. border

- 테두리...

- 내용과 패딩 영역 둘러싸는 테두리

- border 속성 

  - border-style
    - dotted : 점선, dashed : 긴 점선 ... 
  - border-width
    - 테두리의 두께 설정 
  - border-color
    - 테두리 색상 설정 

- top, right, bottom, left (상하좌우) 개별적으로 스타일 적용 가능 

- shorthand

  - ```css
    .border{
        border: 2px dashed black;     
    }
    ```

---

#### 4-4. box-sizing 

- 기본적으로 모든 요소의 box-sizing은 content-box
  - 순수 contents 영역만을 box로 지정
  - contents + margin + padding + border로 인해 실제 크기는 더 커질 수 있다.
- box-sizing을 **border-box** 로 설정
  - margin + padding + border + content 포함한 크기는 지정한 숫자만큼 ,, 



### 5. CSS Display

#### 5-1. display : block 

- 줄 바꿈이 일어나는 요소
- 화면 크기 전체의 가로 폭 차지
  - 가질 수 있는 너비의 100%
  - 가로 꽉꽉 채워서 가져간다
- 블록 요소 안에 인라인 요소 들어갈 수 있다!
- 대표 block  요소 
  - div, ul, ol, li, p, hr, form

---

#### 5-2. display: inline

-  줄 바꿈 일어나지 않는 행의 일부 요소
- content 너비만큼만 가로 폭 차지
- width, height, margin-top, margin-bottom 지정 불가 ㅠㅠ 
- 상하 여백 : line-height로 지정
- 대표 inline 요소 
  - span, a, img, input, label, b, em, i, strong 

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

- HTML 문서 상에서 요소가 배치되는 방식 ( 문서 상에서 요소 위치를 지정할 때 사용)
- top, left, bottom, right 속성과 같이 사용! 
- position으로 위치 기준 변경

- static : 모든 태그의 기본 값 (기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소 위치 기준으로 배치

---

#### 6-1. relative 상대위치 

- 자기 자신의 static 위치 기준으로 이동
  - 자기 위치 + tlbr(top left bottom right) 만큼 이동
- 레이아웃에서 요소가 차지하는 공간은 static 일 때와 같음
- normal flow 유지

```css
# 지금 위치로부터 top 28 left 28 만큼 이동

div {
    position: relative;
    top: 28px;
    left: 28px;
}
```

---

#### 6-2. absolute 절대위치

- 요소를 일반적인 문서 흐름에서 제거 (레이아웃에 공간 차지 X)
- position이 static이 아닌 첫번째 상위요소 따라감
  - 다 static인 경우 body 따라간다.
  - 상위요소 위치에서 tlbr(top left bottom right) 만큼 떨어져있음.
- 보통 복잡해서 부모요소 `<div>`로 지정하고 `relative` 지정
- normal flow에서 벗어남! 앞뒤요소랑 상호작용 X

```css
# 상위요소로부터 top 28 left 28 만큼 이동

div {
    position: absolute;
    top: 28px;
    left: 28px;
}
```

---

#### 6-3. fixed 고정위치

- 요소를 일반적인 문서 흐름에서 제거 (레이아웃에 공간 차지 X)
- 부모 요소와 관계 X viewport (브라우저 전체)기준으로 이동 
  - 스크롤 시 항상 같은 곳에 위치
  - 브라우저 위치에서 tlbr(top left bottom right) 만큼 떨어져있음.
- normal flow에서 벗어남! 앞뒤요소랑 상호작용 X

```css
# 브라우저 기준 top부터 28px left부터 28px 떨어져 있음

div {
    position: fixed;
    top: 28px;
    left: 28px;
}
```

---

#### 6-4. sticky 

- 요소가 스크롤링 될 때 효과 나타남!  





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

#### 7-2. Flex 속성 

- 배치 설정
  - flex-direction
  - flex-wrap
- 공간 나누기
  - **justify-content (main axis)**
  - align-content (cross axis) (안나온다)
- 정렬
  - **align-items (모든 아이템 cross axis 기준)**
  - align-self (개별 아이템)

---

##### 1. flex-direction

- main axis 기준 방향 설정
- 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의 

![image-20220212232248321](과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220212232248321.png)

```
# CSS 

- row : 왼 -> 오 (기본)
- row-reverse : 오 -> 왼
- column : 위 -> 아래
- column-reverse : 아래 -> 위 
```

```
# Bootstrap

- flex-row
- flex-row-reverse
- flex-column
- flex-column-reverse
```



##### 2. flex-wrap

- 요소들이 강제로 한 줄에 배치 되게 할 것인가 ??????? 여부 설정
- 아이템이 컨테이너 벗어나는 경우 해당 영역 내에 배치되도록 설정
- 기본적으로 컨테이너 영역 안벗어남! 

![image-20220212232424092](과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220212232424092.png)

```
- nowrap (기본 값) : 한줄에 배치
- wrap : 넘치면 그 다음 줄로 배치
```



##### + flex-flow

- **flex-direction, flex-wrap**의 shorthand
- flex-direction, flex-wrap에 대한 설정 값 차례로 작성 

```css
flex-flow: row nowrap; <- 기본값들 .. 
```



##### 3. justify-content

- main axis 기준으로 공간 배분 

![image-20220212232812328](과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220212232812328.png)

```
- flex-start (기본값) : 아이템들을 axis 시작점으로
- flex-end : 아이템들을 axis 끝 쪽으로
- center : 아이템들을 axis 중앙으로
- space-between : 아이템 사이의 간격을 균일하게 분배 (시작과 끝에 배치)
- space-around : 아이템 둘러싼 영역 균일하게 분배 (가질 수 있는 영역 나눠서 양쪽에 분배)
- space-evenly : 전체 영역에서 아이템 간격 균일하게! 
```



##### 4. align-content (시험 X)

- cross axis 기준으로 공간 배분
- 아이템이 한 줄로 배치되는 경우 확인할 수 없음 

![image-20220212232908550](과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220212232908550.png)



##### 5. align-items

- 모든 아이템 cross axis 기준으로 정렬

![image-20220212233240738](과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220212233240738.png)

```
- stretch (기본 값) : 컨테이너 가득 채움 
- flex-start : 교차축 방향 시작
- flex-end : 교차축 방향 끝
- center : 교차축 방향 중앙 (수직, 수평 정렬할 때 주로 쓴다.. )
- baseline : 텍스트 baseline에 기준선 맞춤! 
```



##### 6. align-self

- 개별 아이템을 cross axis 기준으로 정렬
- 컨테이너 적용 XXXXXXX 개별 아이템에 적용 

![image-20220212233344613](과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220212233344613.png)



##### + 기타 속성

- flex-grow : 남은 영역을 아이템에 분배 
- order : 배치 순서

---

### 8. CSS 추가 개념들

1. pseudo-class
   - 선택자에 추가하는 키워드 
   - 선택한 요소가 특별한 상태여야 만족할 수 있다!  

```css
selector:pseudo-class {
    property: value;
}
```

- : nth-child(n)
  - 위에서부터 순서대로 세서 n번째 자식요소 

```css
id의 자식요소 중 n번째 값만 변경

#id > p:nth-child(n) {
    color; pink;
}
```

- : nth-of-type(n)
  - type을 만족하는 ! n번째 자식 

```css
id의 자식요소 중 p의 n번째 값만 변경

#id > p:nth-of-type(n) {
    color; pink;
}
```





## Bootstrap

### 1. About Bootstrap

#### 1-1. CDN 

- Content Delivery(Distribution) Network
- 컨텐츠(CSS, JS, Image, Text 등) 효율적 전달하기 위해 여러 노드에 가진 네트워크에 데이터 제공하는 시스템
- 장점
  - 개별  end-user의 가까운 서버 통해 빠르게 전달 가능 (지리적 이점)
  - 외부 서버 활용함으로서 본인 서버 부하가 적어짐

- `<link href="htttps://cdn.jsdelivr.net/ .....">` 처럼 링크 복사해서 사용

---

### 2. spacing, display, position

- Spacing
  - CSS에서 마진, 패딩 주던 것 / em, rem으로 font 크기 지정하는 것 
  - 조합해서 사용하면 된다 .. 

![image-20220212234147142](과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220212234147142.png)

- display

```css
d-inline
d-block
```

- position

```css
d-flex 

justify-content-start
align-items-start
align-self-start 
```



### 3. Responsive Web Design 반응형 웹

- 다양한 화면 크기 가진 디바이스들 등장에 따라 responsive web design 개념 등장! 
- 반응형 웹
  - 별도의 기술 이름 아님!!!!!
  - 웹 디자인에 대한 접근 방식, 도움 되는 사례 모음 표현에 사용되는 용어 
- Media Queries, Flexbox, Bootstrap Grid System, The viewport meta tag .. 



### 4. Bootstrap Grid System

- Grid system (web design에서 .. )

  - 요소들의 디자인과 배치에 도움 주는 시스템
  - 기본 요소
    - column  : 실제 컨텐츠 포함하는 부분
    - gutter : 칼럼과 칼럼 사이 공간 (간격)
    - container : 칼럼 담고 있는 공간

- Bootstrap Grid system

  - flexbox로 제작됨

  - **container, row, column** 으로 컨텐츠 배치하고 정렬 

  - 꼭 기억할 2가지

    1. 화면 => 12개의 column으로 이루어짐

    2. 6개의 grid breakpoint



#### 4-1. Grid system 구조

- 컨테이너 
  - 그리드 시스템 사용할 때 필요! 
  - 가장 기본적인 레이아웃 요소 
  - 칼럼 담고 있는 공간
- column
  - 화면은 총 12개의 칼럼으로 이루어짐 (백분율이라 크기 유동적)

![image-20220213025800544](과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220213025800544.png)

- `.col-(breakpoint)-(column)` 처럼 클래스 만들어서 사용 
  - breakpoint : 그리드 옵션 / 뷰포트 크기에 따라 어떻게 보일지 결정 
  - column :  한 화면에 보여줄 컨텐트의 너비 (12이하의 정수)

```html
# grid system 기본 구조

<div class="container">
    <div class="row">
        <div class="col"></div>
    </div>
</div>
```



- `offset`  : col 여백주기 
  - 지정된만큼 간격 두고 배치하고 싶을 때 사용 
  - col-offset-(column) / offset-(column) 으로 사용

```html
# 앞에 1만큼 빈공간 주고 3칸의 컬럼이 위치  

<div class="offset-1 col-3"> </div>
```

---

#### 4-2. Breakpoints 중단점

- 디바이스, 뷰포트 크기에 따라 레이아웃 변경되는 기준!
- 특정 픽셀 조건에 대한 지점 

![image-20220213024350754](과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220213024350754.png)

---

#### 4-3. 활용 예시.. 

1. 너비 **동일**하게 넣는 경우 

   - 그냥 col 만 사용.. 

   ```html
   <div class="container">
       <div class="row">
         <div class="col">.col</div>
         <div class="col">.col</div>
         <div class="col">.col</div>
       </div>
   </div>
   ```



2. 768px 미만인 경우, 각 컬럼이 4칸, 4칸을 양 끝에서 차지하며 가운데 4칸의 빈 공간.  992px 미만인 경우, 4칸의 빈 공간이 앞에 있고 4칸, 4칸의 컬럼이 뒤쪽에 위치
   - 더 작은 크기에서 **offset** 사용했을 경우, 다음 크기에서 offset-(breakpoint)-0으로 **초기화**해야한다! 
   - 아니면 offset 계속 남아있다.. 

![image-20220213031043423](과목평가 대비 HTML, CSS, Bootstrap 정리.assets/image-20220213031043423.png)

```html
<div class="row">
      <div class="item col-4 offset-md-4 offset-lg-7 col-lg-5">
        <p>item1</p>
      </div>
      <div class="item col-4 offset-4 offset-md-0 offset-lg-2 col-lg-8">
        <p>item2</p>
      </div>
    </div>
```



3.  `row row-col` , `row > col` 

- `row row-col` 

  - 행 당 몇 개의 칼럼을 보여줄 것인지 지정 

  ```html
  row-cols-md-2 : 너비가 768px 이상, 992px 미만인 경우 행당 2개
  ```

- `row > col` 

  - 칼럼 하나의 너비를 지정 

  ```html
  cols-md-2 : 너비가 768px 이상, 992px 미만인 경우 2만큼의 넓이 가진다
  ```

  