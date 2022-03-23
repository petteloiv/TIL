## 깃허브 잔디조작



1. 아무 파일이나 생성 후 푸시 



2. 생성한 가장 최근 파일의 푸시 날짜 변경 

```bash
 git commit --amend --no-edit --date "Fri 18 Mar 2022 20:12:54 KST"
```



3. 조작한 파일 반영해서 풀 받기 해주기 

```bash
 git pull --allow-unrelated-histories origin master
```

```
이 다음에 그 bash 메모장 나오는데 :wq 해서 종료해주기
```



4. 다시 git push