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

$ git push -u origin master #master가 작업한 내용을 origin에 입력

$ browser 로그인 후 새로고침
 
+

$ git config user.email petteloiv@gmail.com 

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

- git pull 
  -  원격 저장소의 버전과 로컬 저장소 버전 같게 만드는 것
  -  기존 같은 파일이 로컬에 있어야한다.
  -  원격 저장소가 구 버전이면 불러와도 덮어씌워지지 않는다.
  
  ```bash
  $ git pull origin master
  ```
  
  
  
- git clone
  - 원격 저장소에 있는 내용이 나에게 없을 때 (완전히 새로운 내용)
  - github 주소 복사
  
  ```bash
  $ git clone https://github.com/petteloiv/TIL.git
  ```
  
  - log, commit 등 그대로 남아있다.
  - 이미 해당하는 폴더가 있으면 git clone 사용할 수 없다.





###  

