# Github

##### 명령어 관련 복습 

- 명령어 이후 `-`하나 사용 = 축약어 `--` 두개 사용 = 원래 단어 그대로

- git log 에서 나올 때 `q` 누르기

## 회원가입

### 설정 변경

- main 브랜치를 master 브랜치로 기본값 수정

## 원격 저장소와 로컬 저장소 연결

- 원격 저장소(깃허브), 로컬 저장소 (.git 폴더가 있는 TIL 폴더)

### Repository 생성

- git remote

- git push

```bash
$ git remote add origin # 별명이 origin인 원격 저장소 추가, 한번만 실행 

$ git push -u origin master
```

```bash
$ git init
$ git add
$ git commit -m "" #수정 다 하고 난 이후 한번씩 남기면 된다

$ git remote add origin https://github.com/petteloiv/TIL.git

$ git push -u origin master #master가 작업한 내용을 origin에 입력 # 이 이후에는 git push로만 작성도 가능 $ git push origin master 

$ browser 로그인 후 새로고침
 
+

$ git config user.email petteloiv@gmail.com 
$ git config user.name petteloiv

# 깃에서 관리하고 있는 유저 이메일

```

- 버전 하나씩 수정 끝낼 때마다 add/commit/push 습관 들이기

### .gitignore

- 특정 파일을 **깃에 올리지 않기 위한** 설정 
- https://www.toptal.com/developers/gitignore 통해 검색하면 깃에서 관리하면 안되는 내용 나온다.. 복사해서 .gitignore에다가 저장하면 얘는 빼고 관리
- `.git` 폴더와 완전히 동일한 위치에 생성해야한다. (최상단)
- 프로젝트 시작 전 가장 먼저 생성하고 진행하는 것이 좋다. 

```bash
$ touch .gitignore # 숨김파일 생성

# gitignore 통해 다른이름 저장

$ git status #확인해보면 password 안보이는 것 알 수 있다
```

- 원격 저장소에도 파일이 있고, 로컬에도 이미 있고, 이미 트래킹 중인 파일을 로컬에서만 더 이상 추적하지 않도록 설정

``` bash
$ git update-index --assume-unchanged {file name}
```



- **로컬에 있는 파일 변동 추적 멈춤**
- 원격 저장소에 해당 파일이 이미 있다면 그 파일 삭제 (원격 저장소에 push 할 때 해당 파일 삭제)

```bash
$ git rm --cached {file name}
# 변동 추적만 중지. 파일 삭제되는건 아니다! 
```



- **로컬, 원격 저장소 모두 파일 삭제 후 추적 중지** 

```bash
$ git rm {filename}
```



1. git init / .gitignore (가장 먼저)
2. 혹시 tracking 되고 있다면 추적 멈추거나 파일 삭제 후 추적 중지 가능



### Git으로 받아와서 작업하기

- `git pull `
  
  -  원격 저장소의 버전과 로컬 저장소 버전 같게 만드는 것
  -  기존 같은 파일이 로컬에 있어야한다.
  -  원격 저장소가 구 버전이면 불러와도 덮어씌워지지 않는다.
  
  ```bash
  $ git pull origin master
  ```
  
  - 양쪽에서 작업해 add 했을 경우 원격 저장소의 변화를 통일 시켜줘야한다.
  - 메모장(VIM) 벗어나기 `:wq` = 저장하고 종료할거야 => 변화 업데이트 해준다.
  
- `git clone`

  - 원격 저장소에 있는 내용이 나에게 없을 때 (완전히 새로운 내용)
  - github 주소 복사

  ```bash
  $ git clone https://github.com/petteloiv/TIL.git
  ```

  - log, commit 등 그대로 남아있다.
  - 이미 해당하는 폴더가 있으면 git clone 사용할 수 없다.



### 주의점

- add를 하지 않으면 수정 내용 기록되지 않는다
- file (1,2) 작성 > add, commit > file(3) 수정 = modified 상태 > add > file(4) 수정 
- commit = 중간 세이브 하고싶으면 커밋 진행. 보통 작업 단위별.



#### 문제상황 1

- git 이 우리에게 물어보려는 상황 발생 ! 

1. 집에서 추가 공부 후 add commit push
2. 다음날 강의장에서 pull 받는 걸 까먹고 workshop file 수정 ..  
3. a c p 하려다가 오류나고 새롭게 pull 받음
4. merge failed 발생! 

```bash
user@DESKTOP-0BDFPBP MINGW64 ~/Desktop/SSAFY/TIL (master|MERGING)
```



5. 두개를 합쳐주기는 함.. 하지만 서로 같은 위치라면 git이 다시 물어본다
6. 내가 필요한 부분 남기고 다시 a c p
7. 집에서 다시 pull 받으면 통합된 버전으로 되어있다.  



#### 끝말잇기.. 

1. repository 생성
2. 폴더 -> 파일 -> 시작단어

```bash
# 폴더에서 git bash here
$ git init

$ touch relay.md # 파일 생성
$ start relay.md # 파일 실행

$ git status # 상태 확인
```

3. 원격저장소에 올리기

```bash
$ git add relay.md
$ git commit -m "끝말잇기 시작"

```

```bash
# 내 컴퓨터와 깃 허브 연결

$ git remote add origin https://github.com/petteloiv/relay.git # git아 원격저장소 추가할건데 이름 origin이고 위치는 여기(깃주소)야~ 
# 일반적으로는 원격 저장소 하나만 쓰다 보니까 보통 origin 사용

$ git remote add origin https://github.com/petteloiv/relay.git #이미 있으니까 추가! 

$ git remote -v #연결되었는지 확인 가능 


+ $ git remote remove til #til(원격저장소)에 연결시켜둔거 삭제 
```

```bash
$ git push -u origin master # set-upstream의 약자. 앞으로는 origin 경로에 master 작업내역 push 할거야
```

4. 팀원의 repository 초대 받고 수락 
5.  word 폴더가 없으므로  clone으로 연결

```bash
$ git clone https://github.com/jehaak/word.git
```

6. 폴더 받고 수정 후 

```bash
$ git add
$ git commit
$ git push

$ git pull  반복 
```



#### Branch 브랜치

- 관례적으로 사용하는 브랜치명 정해져있다
  - `master` (성역)  >  `dev`브랜치 > `chat` 기능 있는 브랜치
  - 말 그대로 가지처럼 기능 별 브랜치 생성하고 상위 브랜치로 합친다.



### git branch 명령어

- 브랜치 `생성`, `삭제`,`조회` 명령어

```bash
# 브랜치 조회 (master 있는 상태여야한다.)
$ git branch
* master # 지금 조회하고 있는 브랜치가 master 이다. 
```

```bash
#원격 저장소의 브랜치 목록 확인
$ git branch -r 
```

```bash
# 브랜치 생성
$ git branch {branch name}

# 브랜치 삭제

# 병합된 (수정내역을 합치고 난 후에 삭제 가능)
$ git branch -d {branch name} 

# (주의) 병합되지 않은 브랜치 강제 삭제
$ git branch -D {branch name} 
```



### git switch

- 현재 브랜치에서 다른 브랜치로 `HEAD`를 이동시키는 명령어
- `HEAD`는 현재 브랜치를 가리키는 포인터

```bash
# 다른 브랜치로 이동
$ git switch {다른 브랜치 이름}

# 브랜치를 새로 생성하고 동시에 이동 
$ git switch -c {다른 브랜치 이동}
```



- **주의사항**

  git switch 하기 전에 commit 하셨나요? 

  **switch 하기 전에 그 브랜치에서 만들어뒀던 것 commit 필수!** 

- branch는 협업할 때 주로 사용 



### git merge

```bash
$ git merge dev 

Fast-forward # 두개를 합쳤을 때 새로운 버전 만드는 것이 아니라.. 옮기는것

$ git branch # 더 이상 새로운 것 없으면 브랜치 삭제해준다.
$ git branch -d dev

$ git merge # 눌렀을 때 메모장에 i,a 눌렀을 경우 --끼워넣기-창 등장.. 그냥 엔터 치면 나가짐(?)
```



### git add / commit / push

```bash
$ git add . # 현재 폴더 전부 추가 

# 상위 폴더에 있는 애들은 git add . 으로 추가 불가능! 
# 항상 작업 위치 확인하고 진행하기.
```

 

