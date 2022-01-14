# GITHUB

## 회원가입

### 설정 변경

- main 브랜치를 master 브랜치로 기본값 수정



## 원격 저장소와 로컬 저장소를 연결하는 방법

### repository 생성

- git remote
- git push



```bash
$ git add
$ git commit -m "커밋할 내용"
$ git push
```



## .gitignore

- 원격 저장소에도 파일이 있고, 로컬에도 이미 있고, 이미 트래킹중인 파일을 로컬에서만 더이상 추적하지 않도록 설정

```bash
$ git update-index --assume-unchanged {file name}
```

- 로컬에 있는 파일 변동 추적 멈춤
- 원격 저장소에 해당 파일이 이미 있다면, 그 파일 삭제(원격 저장소에 push할 때 원격 저장소에서 해당 파일 삭제)

```bash
$ git rm --cached {file name}
```

- 로컬, 원격저장소 모두 파일 삭제 후 추적중지

```bash
$ git rm {file name}
```

위의 코드를 이용하면 '삭제 내역'이 남지 않음. (파일 직접삭제와의 차이)

1. git init

2. gitignore

(우선적으로 만들어야 하는 것)





## git clone

repository - code - 복사 - 바탕화면 git bash here - git clone 주소붙여넣기

## git pull originmaster

업데이트된 레포지토리를 받아오려 할 때(해당 깃에대한 정보는 이미 갖고 있을 때) 이용