# BFE-server

## Table of Contents

- [Intro](#intro)
- [Install](#install)
- [Usage](#usage)
- [Branch](#branch)
- [Commit](#commit)
- [Deploy](#deploy)
- [Database](#database)

## Intro

이 레포지토리는 Buying For Earth의 서버 코드를 관리하는 레포지토리 입니다. 

**landing-page** : https://buyingforearth.com/landing

**client repository** : https://github.com/Buying-For-Earth/BFE-client

**server url** : http://ec2-52-79-76-54.ap-northeast-2.compute.amazonaws.com:5000/


## Install

가상환경을 사용합니다. 프로젝트에서는 `pipenv`를 사용했습니다.
```sh
$ pipenv shell
```
실행한 가상환경에 `requirements.txt`파일의 모듈들을 설치해줍니다.
```sh
$ pip install -r requirements.txt
```


## Usage

도커를 통해서 빌드하고 실행해줍니다. 
```sh
$ docker build -t bfeserver .
$ docker run --name bfeflask -p 5000:5000 bfeserver
```

## Branch

`dev` : 개발 레포지토리의 메인 브랜치입니다. 새로운 기능을 추가하는 경우 꼭 이 브랜치에서 새로운 브랜치를 만들어야합니다.

`feature/{name}` : 새로운 기능을 만드는 경우 dev브랜치에서 생성하는 브랜치입니다. 

`fix/{name}` : 버그수정이나 기능 수정이 일어나는 경우 dev브랜치에서 생성하는 브랜치입니다. 

## Commit

태스크 카드 (이슈카드)가 생성되어있는 경우 모든 커밋 메시지는 이슈카드의 번호를 추가해줘야 합니다.

`생성(#{issue-number}){자세한 내용}` : 기능이나 파일이 새로 생성되는 경우 사용하는 커밋메시지 입니다. 

`수정(#{issue-number}){자세한 내용}` : 기능이나 코드가 수정되는 경우 사용하는 커밋메시지 입니다.

`삭제(#{issue-number}){자세한 내용}` : 기능이나 코드, 파일이 삭제되는 경우 사용하는 커밋메시지 입니다.

## Deploy

배포는 배포용 private 레포지토리를 추가해서 진행합니다. 
```sh
$ git remote add deploy {deploy전용 레포지토리 주소}
```
배포는 `dev`브랜치에서 `deploy`브랜치를 생성하여 관리합니다. 
```sh
$ git checkout deploy
$ git pull origin dev
$ git push origin deploy deploy
```
배포용 레포지토리에 push하게 되면 github actions을 통해 자동으로 배포가 진행됩니다. 

빌드 결과와 code deploy로 ec2에 배포되는 결과는 slack의 #server-deploy 채널로 모니터링 할 수 있습니다. 

## Database
데이터베이스의 스키마는 [dbdiagram](https://dbdiagram.io/d/6024dbfc80d742080a3a18c7) 에서 관리되고 있습니다. 

데이터베이스의 스키마가 변경되는 경우 `flask-migrate`를 사용하여 `src/models`에 작성되어있는 모델 파일들을 마이그레이션 해줍니다.

마이그레이션 폴더 생성 (생성이 안되어 있는 경우)
```sh
$ flask db init
```

스키마가 변경되어 `src/models`에 작성되어있는 모델 파일이 수정된 경우 마이그레이션 파일을 만들어줍니다. 
```sh
$ flask db migrate
```

마이그레이션 파일이 생성된 경우 마이그레이션 파일을 실행시켜, 데이터베이스를 변경시켜줍니다.
```sh
$ flask db upgrade
```

만약 이전상태로 돌려야하는 경우
```sh
$ flask db downgrade
```






