# 🍀PLANTINUM

<div align="center">
  <img src="./README.assets/logo.png" width="60%">
</div>

**PLANTinum** 이란 **Plant + Platinum** 의 합성어입니다. 또한, **plan**을 의미하기도 해서 계획적으로 식물을 관리하고 보살핀다는 의미를 담고있습니다. 본 프로젝트는 반려식물을 자동으로 케어해주고 나아가 웹을 통하여 이렇게 기른 반려식물을 거래할 수 있게 만드는 **IoT 플랫폼 서비스** 개발을 목표로 합니다.



보다 자세한 내용은 Wiki를 참고해 주세요.

> [Wiki](https://lab.ssafy.com/s07-webmobile3-sub2/S07P12A109/-/wikis/home)



## 💾설치

사이트 주소 : [Plantinum](http://plantinum.co.kr)

> 자세한 내용은 [포팅 매뉴얼](./exec) 참고

- FE
> 파일 위치 : ./FE/plantinum
```shell
// 배포용 설치
$ npm run build

// 로컬에서 이용시 설치
$ npm i
$ npm run serve
```

- BE
> 파일 위치 : ./BE/back

```shell
$ python manage.py runserver
```


- CHAT

> 파일 위치 : ./BE/chat
```shell
$ nohup node app.js &
```



## 🌸 IoT

[코드정보](./HW/Supool)

### [Supool](./HW/Supool)
> 라즈베리파이에 다운로드 후 폴더 내에서 다음 명령어 실행
```shell
$ python main.py
```

### [외관](./HW/stl_files)
> SuPool의 외관 3D 디자인



## 🌸WEB 
### 🌻FE
[코드정보](./FE/) 참고

>  [플랜티넘 폴더](./FE/plantinum/)에서 vscode 실행 후 api 연결 포트 선택

```js
// /FE/plantinum/src/api/drf.js

// 로컬에서 실행할 경우
const HOST = 'http://127.0.0.1:8000/api/v1/'

// 배포용 api 주소
// const HOST = 'http://plantinum.co.kr/api/v1/'
```


### 🌻BE
[api 가이드 문서.md](./BE/api%20%EA%B0%80%EC%9D%B4%EB%93%9C%20%EB%AC%B8%EC%84%9C.md) 참고

[채팅 서버 구축 문서.md](./BE/uwsgi%EB%A5%BC%20%EC%9D%B4%EC%9A%A9%ED%95%B4%EC%84%9C%20django%EC%99%80%20nginx%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0.md) 참고



## 🎮기술스택
[기술스택정리문서](./Docs/STACK_EXPLANATION.md)




## 📃Docs
[문서 모음](./Docs/)
> [프로젝트_명세서](./Docs/%5B%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8_%EB%AA%85%EC%84%B8%EC%84%9C%5DPlantinum.docx) : 프로젝트가 수행해야 할 모든 기능과 제약 사항, 서비스적인 요구사항을 분석해서 기록해둔 문서

> [HW 흐름 구상 및 유즈케이스.docx](./Docs/HW%20%ED%9D%90%EB%A6%84%20%EA%B5%AC%EC%83%81%20%EB%B0%8F%20%EC%9C%A0%EC%A6%88%EC%BC%80%EC%9D%B4%EC%8A%A4.docx) : 하드웨어 흐름 구상도

> [Jira_guide.pdf](./Docs/Jira_guide.pdf) : Jira 사용법 정리

> [STACK_EXPLANATION](./Docs/STACK_EXPLANATION.md) : 기술 스택 정리




## 💿ERD
 [ERD](https://www.erdcloud.com/d/BqMQqe8yrRaQ5PXyd)

![erd](README.assets/erd.png)
