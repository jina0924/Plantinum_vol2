# 0. 목차

### 목차
[TOC]

### 시작하기

```python
python manage.py migrate
python manage.py loaddata plants.json juso.json user.json myplant.json leaf82.json
```

```
# 생성되어있는 유저
plantinum_test
plantinum_test2
```



# 1. 관리자 페이지

```
http://127.0.0.1:8000/admin/
```



# 2. 유저 관련 페이지

### 회원가입

- 회원가입시 자동으로 로그인 상태로 변경됨
- 토큰 생성 및 리턴
- POST

- URL

```
http://127.0.0.1:8000/api/v1/accounts/signup/
```

- Body

| Key          | Type   | Description     | Mandatory | Example        |
| ------------ | ------ | --------------- | --------- | -------------- |
| username     | String | 유저아이디      | O         | plantinum_test |
| email        | String | 이메일          | O    | plantinum_test@testemail.com |
| password1    | String | 비밀번호        | O         | xptmxmdlqslek |
| password2    | String | 비밀번호 재입력 | O         | xptmxmdlqslek |
| phone_number | String | 폰넘버          |           |     |
| addr         | String | 주소            |           |           |
| zip_code     | String | 우편번호        |           |           |
| nickname     | String | 닉네임, default값 존재         |           |  |

- Response

```
{
    "key": "3e2df1dc87c527fc5722b907f48e352dd3c046ee"
}
```



### 로그인

- 토큰 리턴
- POST
- URL

```
http://127.0.0.1:8000/api/v1/accounts/login/
```

- Body

| Key      | Type   | Description | Mandatory | Example        |
| -------- | ------ | ----------- | --------- | -------------- |
| username | String | 유저아이디  | O         | plantinum_test |
| password | String | 비밀번호    | O         | xptmxmdlqslek  |

- Response

```
{
    "key": "57f72c606b9cbd10d2ecf5df6eda4b90f2213198"
}
```



### 로그아웃

- 로그인 사용자 - 토큰 사용

- POST

- URL

```
http://127.0.0.1:8000/api/v1/accounts/logout/
```

- Headers

| Key           | Type   | Description   | Mandatory | Example                                        |
| ------------- | ------ | ------------- | --------- | ---------------------------------------------- |
| Authorization | String | Token {token} | O         | Token 3e2df1dc87c527fc5722b907f48e352dd3c046ee |

- Response

```
{
    "detail": "로그아웃되었습니다."
}
```



### 비밀번호 변경

- 로그인 사용자 - 토큰 사용
- POST
- URL

```
http://127.0.0.1:8000/api/v1/accounts/password/change/
```

- Body

| Key           | Type   | Description | Mandatory | Example           |
| ------------- | ------ | ----------- | --------- | ----------------- |
| new_password1 | String |             | O         | new_xptmxmdlqslek |
| new_password1 | String |             | O         | new_xptmxmdlqslek |

- Response

```
{
    "detail": "새로운 패스워드가 저장되었습니다."
}
```



### 마이페이지(프로필)

- 잎팔이 글 전체 조회 추가예정
- 나의 프로필만 확인 가능, 다른 사람의 프로필 확인 X
- 로그인 사용자 - 토큰 사용
- GET
- URL

```
http://127.0.0.1:8000/api/v1/accounts/profile/
```

- Response

```
{
    "pk": 1,
    "nickname": "싱싱한소나무3309",
    "email": "plantinum_test@testemail.com",
    "phone_number": "",
    "addr": "",
    "zip_code": "",
    "myplant_count": 4,
    "dday": 1,
    "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/static/profile.jpg",
    "leaf82_set": [
        {
            "pk": 1,
            "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/images/leaf82/%EB%AC%B4%EB%8A%AC%EC%82%B0%ED%98%B8%EC%88%98.jpg",
            "posting_addr": 893570,
            "plantname": "무늬산호수"
        },
        {
            "pk": 2,
            "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/images/leaf82/%EC%82%B0%EC%84%B8%EB%B2%A0%EB%A6%AC%EC%95%84.jpg",
            "posting_addr": 863022,
            "plantname": "산세베리아"
        },
        {
            "pk": 3,
            "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/static/monstera.jpg",
            "posting_addr": 883823,
            "plantname": "치자나무"
        }
    ]
}
```



### 회원정보수정

- 닉네임, 이메일, 핸드폰번호, 주소, 우편번호, 사진만 수정 가능
- 비밀번호 변경은 별개의 요청
- 로그인 사용자 - 토큰 사용
- PUT
- URL

```
http://127.0.0.1:8000/api/v1/accounts/userinformation/
```

- Body

| Key          | Type      | Description                   | Mandatory | Example                      |
| ------------ | --------- | ----------------------------- | --------- | ---------------------------- |
| nickname     | String    |                               | O         | 플랜티넘테스트               |
| email        | String    |                               | O         | plantinum_test@testemail.com |
| phone_number | String    |                               | O         |                              |
| addr         | String    |                               | O         |                              |
| zip_code     | String    |                               | O         |                              |
| photo        | ImageFile | 새로운 사진/기존사진/기본사진 | O         |                              |

- Response

```
{
    "pk": 1,
    "nickname": "플랜티넘테스트",
    "email": "plantinum_test@testemail.com",
    "phone_number": "",
    "addr": "",
    "zip_code": "",
    "myplant_count": 4,
    "dday": 1,
    "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/static/profile.jpg"
}
```



### 회원탈퇴

- 로그인 사용자 - 토큰 사용
- DELETE
- URL

```
http://127.0.0.1:8000/api/v1/accounts/withdraw/
```

- Response

```
{
    "detail": "정상적으로 탈퇴되었습니다."
}
```



# 3. 식물 관련 페이지

### 전체 식물 데이터 조회

- 공공데이터를 활용한 식물 데이터
- 확인용O 배포용X
- GET
- URL

```
http://127.0.0.1:8000/api/v1/plants/
```

- Response

```
[
    {
        "id": 1,
        "myplant_set": [
            {
                "pk": 2,
                "nickname": "가울이"
            }
        ],
        "name": "가울테리아",
        "watercycle_spring": "053003",
        "watercycle_spring_nm": "토양 표면이 말랐을때 충분히 관수함",
        "watercycle_summer": "053003",
        "watercycle_summer_nm": "토양 표면이 말랐을때 충분히 관수함",
        "watercycle_autumn": "053003",
        "watercycle_autumn_nm": "토양 표면이 말랐을때 충분히 관수함",
        "watercycle_winter": "053004",
        "watercycle_winter_nm": "화분 흙 대부분 말랐을때 충분히 관수함",
        "specl_manage_info": ""
    },
    ...
]
```



### 등록용 식물 검색

- 물주기 등록시 사용
- 로그인 사용자 - 토큰 사용
- GET
- URL

```
http://127.0.0.1:8000/api/v1/plants/search/
```

- Response

```
[
    {
        "pk": 1,
        "name": "가울테리아"
    },
    {
        "pk": 2,
        "name": "개운죽"
    },
    ...
    {
        "pk": 207,
        "name": "직접 입력하기"
    }
]
```



### 내식물 전체 조회

- 로그인 사용자 - 토큰 사용
- GET
- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{username}/
```

- Request Parameters

| Name     | Type   | Description | Mandatory | Example        |
| -------- | ------ | ----------- | --------- | -------------- |
| username | String | 유저id      | O         | plantinum_test |

- Response

```
[
    {
        "pk": 4,
        "nickname": "개나리아님",
        "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/images/myplant/%EC%98%81%EC%B6%98%ED%99%94.jpg",
        "sensing": {
            "moisture_level": 0
        },
        "diary_count": 0
    },
    {
        "pk": 3,
        "nickname": "중간고사",
        "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/images/myplant/%EB%B2%9A%EB%82%98%EB%AC%B4.jpg",
        "sensing": {
            "moisture_level": 0
        },
        "diary_count": 0
    },
    {
        "pk": 2,
        "nickname": "가울이",
        "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/images/myplant/%EA%B0%80%EC%9A%B8%ED%85%8C%EB%A6%AC%EC%95%84.jpg",
        "sensing": {
            "moisture_level": 0
        },
        "diary_count": 0
    },
    {
        "pk": 1,
        "nickname": "사랑이",
        "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/images/myplant/%EB%9F%AC%EB%B8%8C%EC%B2%B4%EC%9D%B8.jpg",
        "sensing": {
            "moisture_level": 0
        },
        "diary_count": 0
    }
]
```



### 내식물 등록

- 물주기 등록 전 반드시 식물 이름 검색이 선행되어야 함
- 로그인 사용자 - 토큰 사용
- POST
- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/
```

- Body

| Key      | Type   | Description                  | Mandatory | Example |
| -------- | ------ | ---------------------------- | --------- | ------- |
| nickname | String | 내식물 등록 대상 식물의 애칭 | O         | 깨운이  |
| photo    | ImageFile | 내식물 등록 대상 식물의 사진 | 기본값존재 |         |
| plantname | String | 사용자가 선택한 식물 이름 | O    | 개운죽     |
| tmp | String | 직접 입력하기 선택시 기입 |  |  |

- Response

```
{
    "id": 8,
    "user": {
        "pk": 1,
        "username": "plantinum_test",
        "nickname": "플랜티넘테스트"
    },
    "plant_info": {
        "pk": 2,
        "name": "개운죽",
        "watercycle_spring_nm": "흙을 촉촉하게 유지함(물에 잠기지 않도록 주의)",
        "watercycle_summer_nm": "흙을 촉촉하게 유지함(물에 잠기지 않도록 주의)",
        "watercycle_autumn_nm": "흙을 촉촉하게 유지함(물에 잠기지 않도록 주의)",
        "watercycle_winter_nm": "토양 표면이 말랐을때 충분히 관수함",
        "specl_manage_info": "수경은 물주기가 필요 없으나, 화분은 1-2주에 한번씩 충분히 관수한다."
    },
    "sensing": {
        "id": 8,
        "remaining_water": false,
        "state_led": false,
        "moisture_level": 0,
        "last_watering": "",
        "my_plant": 8
    },
    "diary_set": [],
    "diary_count": 0,
    "nickname": "깨운이",
    "created_at": "2022-08-13T22:41:15.882334",
    "otp_code": null,
    "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/static/monstera.jpg",
    "is_connected": false,
    "tmp": ""
}
```



### 내식물 상세페이지

- 물주기 식물 별 상세페이지
- 로그인 사용자 - 토큰 사용
- GET
- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{내식물 식물 pk}/detail/
```

- Request Parameters

| Name           | Type | Description             | Mandatory | Example |
| -------------- | ---- | ----------------------- | --------- | ------- |
| 내식물 식물 pk | Int  | 내식물 등록한 식물의 pk | O         | 8       |

- Response

```
{
    "id": 8,
    "user": {
        "pk": 1,
        "username": "plantinum_test",
        "nickname": "플랜티넘테스트"
    },
    "plant_info": {
        "pk": 2,
        "name": "개운죽",
        "watercycle_spring_nm": "흙을 촉촉하게 유지함(물에 잠기지 않도록 주의)",
        "watercycle_summer_nm": "흙을 촉촉하게 유지함(물에 잠기지 않도록 주의)",
        "watercycle_autumn_nm": "흙을 촉촉하게 유지함(물에 잠기지 않도록 주의)",
        "watercycle_winter_nm": "토양 표면이 말랐을때 충분히 관수함",
        "specl_manage_info": "수경은 물주기가 필요 없으나, 화분은 1-2주에 한번씩 충분히 관수한다."
    },
    "sensing": {
        "id": 8,
        "remaining_water": false,
        "state_led": false,
        "moisture_level": 0,
        "last_watering": "",
        "my_plant": 8
    },
    "diary_set": [],
    "diary_count": 0,
    "nickname": "깨운이",
    "created_at": "2022-08-13T22:41:15.882334",
    "otp_code": null,
    "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/static/monstera.jpg",
    "is_connected": false,
    "tmp": ""
}
```



### 내식물 수정

- 닉네임과 사진만 수정 가능

- 로그인 사용자 - 토큰 사용

- PUT
- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{내식물 식물 pk}/detail/
```

- Request Parameters

| Name           | Type | Description             | Mandatory | Example |
| -------------- | ---- | ----------------------- | --------- | ------- |
| 내식물 식물 pk | Int  | 내식물 등록한 식물의 pk | O         | 8       |

- Body

| Key      | Type   | Description                                                  | Mandatory | Example |
| -------- | ------ | ------------------------------------------------------------ | --------- | ------- |
| nickname | String | 내식물 등록 대상 식물의 애칭                                 | O         | 깨운잉  |
| photo    | String | 내식물 등록 대상 식물의 사진<br />새로운 사진/기존사진/기본사진 | O         |         |

- Response

```
{
    "id": 8,
    "user": {
        "pk": 1,
        "username": "plantinum_test",
        "nickname": "플랜티넘테스트"
    },
    "plant_info": {
        "pk": 2,
        "name": "개운죽",
        "watercycle_spring_nm": "흙을 촉촉하게 유지함(물에 잠기지 않도록 주의)",
        "watercycle_summer_nm": "흙을 촉촉하게 유지함(물에 잠기지 않도록 주의)",
        "watercycle_autumn_nm": "흙을 촉촉하게 유지함(물에 잠기지 않도록 주의)",
        "watercycle_winter_nm": "토양 표면이 말랐을때 충분히 관수함",
        "specl_manage_info": "수경은 물주기가 필요 없으나, 화분은 1-2주에 한번씩 충분히 관수한다."
    },
    "sensing": {
        "id": 8,
        "remaining_water": false,
        "state_led": false,
        "moisture_level": 0,
        "last_watering": "",
        "my_plant": 8
    },
    "diary_set": [],
    "diary_count": 0,
    "nickname": "깨운잉",
    "created_at": "2022-08-13T22:41:15.882334",
    "otp_code": null,
    "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/static/monstera.jpg",
    "is_connected": false,
    "tmp": ""
}
```



### 내식물 삭제

- 로그인 사용자 - 토큰 사용

- DELETE
- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{내식물 식물 pk}/detail/
```

- Request Parameters

| Name           | Type | Description             | Mandatory | Example |
| -------------- | ---- | ----------------------- | --------- | ------- |
| 내식물 식물 pk | Int  | 내식물 등록한 식물의 pk | O         | 8       |

- Response

```
{
    "detail": "내식물이 삭제되었습니다."
}
```



### OTP 생성

- 기기와 연결되지 않았고 OTP도 없는 상태에서 OTP 발급
- 연결이 되지 않았는데 OTP가 있다면 현재 있는 값 보여주기
- 20초 후 자동으로 삭제 (NULL)

- 로그인 사용자 - 토큰 사용
- GET

- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{내식물 식물 pk}/otp/
```

- Request Parameters

| Name           | Type | Description             | Mandatory | Example |
| -------------- | ---- | ----------------------- | --------- | ------- |
| 내식물 식물 pk | Int  | 내식물 등록한 식물의 pk | O         | 1       |

- Response

```
# 정상 발급 / otp 존재
{
    "otp_code": "492279"
}
```

```
# 연결된 상태
{
    "detail": "이미 연결되었습니다."
}
```

```
# 존재하지 않는 식물pk
{
    "detail": "찾을 수 없습니다."
}
```

```
# 다른 유저의 식물
{
    "detail": "잘못된 접근입니다."
}
```



### OTP 상태 조회

- 식물의 OTP 상태 조회
- 값이 있으면 해당 값 리턴, 없으면 null 리턴
- 로그인 사용자 - 토큰 사용
- GET
- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{내식물 식물 pk}/otp/status/
```

- Request Parameters

| Name           | Type | Description             | Mandatory | Example |
| -------------- | ---- | ----------------------- | --------- | ------- |
| 내식물 식물 pk | Int  | 내식물 등록한 식물의 pk | O         | 1       |

- Response

```
{
    "otp_code": "636631"
}
```

```
{
    "otp_code": null
}
```



### 연결 해제

- 기기와 연결상태가 True인 경우 연결 해제
- 로그인 사용자 - 토큰 사용

- GET
- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{내식물 식물 pk}/disconnect/
```

- Request Parameters

| Name           | Type | Description             | Mandatory | Example |
| -------------- | ---- | ----------------------- | --------- | ------- |
| 내식물 식물 pk | Int  | 내식물 등록한 식물의 pk | O         | 1       |

- Response

```
# 정상 연결 해제
{
	"is_connected": false
}
```

```
# 연결되지 않은 식물의 연결 해제 시도
{
    "detail": "연결상태를 확인해주세요."
}
```



### 식물 일지

- **수정필요**

- 나의 식물 별 일지 전체 조회, 일지 작성
- 로그인 사용자 - 토큰 사용
- GET, POST
- PUT/DELETE는 추후 추가 예정
- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{내식물 식물 pk}/diary/
```

- Request Parameters

| Name           | Type | Description | Mandatory | Example |
| -------------- | ---- | ----------- | --------- | ------- |
| 내식물 식물 pk | Int  |             | O         | 2       |

- Body: POST

| Key            | Type   | Description                   | Mandatory | Example            |
| -------------- | ------ | ----------------------------- | --------- | ------------------ |
| content        | String |                               | O         | 쑥쑥 자라는 가울이 |
| photo          | String | **수정 예정**                 | 임시 X    |                    |
| public_private | Bool   | default=False<br />False=공개 |           |                    |

- Response

```
# GET
[
    {
        "id": 1,
        "my_plant": {
            "pk": 2,
            "nickname": "가울이"
        },
        "content": "첫 번째 일지",
        "photo": "",
        "diary_created_at": "2022-07-26T08:15:09.427783Z",
        "public_private": false
    },
    {
        "id": 2,
        "my_plant": {
            "pk": 2,
            "nickname": "가울이"
        },
        "content": "두 번째 일지",
        "photo": "",
        "diary_created_at": "2022-07-26T08:16:08.831901Z",
        "public_private": false
    }
]
```

```
# POST
{
    "id": 3,
    "my_plant": {
        "pk": 2,
        "nickname": "가울이"
    },
    "content": "쑥쑥 자라는 가울이",
    "photo": "",
    "diary_created_at": "2022-07-26T08:32:50.126572Z",
    "public_private": false
}
```



# 4. 잎팔이 관련 페이지

### 지역(시도) 조회

- GET
- URL

```
http://127.0.0.1:8000/api/v1/leaf82/search/sido/
```

- Response

```
[
    {
        "sido": "서울특별시"
    },
    {
        "sido": "부산광역시"
    },
    {
        "sido": "대구광역시"
    },
    {
        "sido": "인천광역시"
    },
    {
        "sido": "광주광역시"
    },
    {
        "sido": "대전광역시"
    },
    {
        "sido": "울산광역시"
    },
    {
        "sido": "경기도"
    },
    {
        "sido": "강원도"
    },
    {
        "sido": "충청북도"
    },
    {
        "sido": "충청남도"
    },
    {
        "sido": "전라북도"
    },
    {
        "sido": "전라남도"
    },
    {
        "sido": "경상북도"
    },
    {
        "sido": "경상남도"
    },
    {
        "sido": "제주특별자치도"
    }
]
```



### 동네(시군구) 조회

- GET
- URL

```
http://127.0.0.1:8000/api/v1/leaf82/search/{시도}/sigungu/
```

- Request Parameters

| Name | Type   | Description | Mandatory | Example        |
| ---- | ------ | ----------- | --------- | -------------- |
| 시도 | String | 한글명      | O         | 제주특별자치도 |

- Response

```
[
    {
        "pk": 259,
        "sigungu": "제주시"
    },
    {
        "pk": 260,
        "sigungu": "서귀포시"
    }
]
```



### 잎팔이 글 생성

- 시도/시군구 순차적 검색 필요
- 로그인 사용자 - 토큰 사용
- POST
- URL

```
http://127.0.0.1:8000/api/v1/leaf82/new/
```

- Body

| Key            | Type   | Description                                    | Mandatory  | Example    |
| -------------- | ------ | ---------------------------------------------- | ---------- | ---------- |
| sido           | String | 시도                                           | O          | 서울특별시 |
| sigungu        | String | 시군구                                         | O          | 종로구     |
| plantname      | String | 식물이름                                       | O          | 산세베리아 |
| content        | Text   | 내용                                           | O          | 채팅주세요 |
| price          | Int    | 가격                                           | O          | 20000      |
| category_class | String | 분양해요/분양받아요                            | O          | 분양해요   |
| status_class   | String | 분양대기/분양완료/분양예약<br />default=판매중 |            |            |
| photo          | Text   |                                                | 기본값존재 |            |

- Response

```
{
    "id": 6,
    "user": {
        "pk": 1,
        "username": "plantinum_test",
        "nickname": "플랜티넘테스트",
        "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/static/profile.jpg"
    },
    "addr": {
        "id": 1,
        "sido": "서울특별시",
        "sigungu": "종로구"
    },
    "plantname": "산세베리아",
    "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/static/monstera.jpg",
    "created_at": "2022-08-13T22:58:26.972836",
    "content": "채팅주세요",
    "price": 20000,
    "category_class": "분양해요",
    "status_class": "분양대기",
    "posting_addr": 350230
}
```



### 잎팔이 글  전체 조회

- 잎팔이 글 전체 조회 (지역 상관 X)
- 최신순으로 조회
- GET
- URL

```
http://127.0.0.1:8000/api/v1/leaf82/main
```

- Response

```
[
    {
        "pk": 6,
        "plantname": "산세베리아",
        "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/static/monstera.jpg",
        "price": 20000,
        "category_class": "분양해요",
        "status_class": "분양대기",
        "addr": {
            "id": 1,
            "sido": "서울특별시",
            "sigungu": "종로구"
        },
        "posting_addr": 350230,
        "user": {
            "pk": 1,
            "username": "plantinum_test"
        }
    },
    {
        "pk": 5,
        "plantname": "라일락",
        "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/images/leaf82/%EB%9D%BC%EC%9D%BC%EB%9D%BD.jpg",
        "price": 100000,
        "category_class": "분양해요",
        "status_class": "분양대기",
        "addr": {
            "id": 5,
            "sido": "서울특별시",
            "sigungu": "광진구"
        },
        "posting_addr": 415916,
        "user": {
            "pk": 2,
            "username": "plantinum_test2"
        }
    },
    {
        "pk": 4,
        "plantname": "아몬드페페",
        "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/static/monstera.jpg",
        "price": 10900,
        "category_class": "분양받아요",
        "status_class": "분양대기",
        "addr": {
            "id": 23,
            "sido": "서울특별시",
            "sigungu": "강남구"
        },
        "posting_addr": 938738,
        "user": {
            "pk": 2,
            "username": "plantinum_test2"
        }
    },
    {
        "pk": 3,
        "plantname": "치자나무",
        "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/static/monstera.jpg",
        "price": 0,
        "category_class": "분양받아요",
        "status_class": "분양대기",
        "addr": {
            "id": 4,
            "sido": "서울특별시",
            "sigungu": "성동구"
        },
        "posting_addr": 883823,
        "user": {
            "pk": 1,
            "username": "plantinum_test"
        }
    },
    {
        "pk": 2,
        "plantname": "산세베리아",
        "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/images/leaf82/%EC%82%B0%EC%84%B8%EB%B2%A0%EB%A6%AC%EC%95%84.jpg",
        "price": 35000,
        "category_class": "분양해요",
        "status_class": "분양대기",
        "addr": {
            "id": 23,
            "sido": "서울특별시",
            "sigungu": "강남구"
        },
        "posting_addr": 863022,
        "user": {
            "pk": 1,
            "username": "plantinum_test"
        }
    },
    {
        "pk": 1,
        "plantname": "무늬산호수",
        "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/images/leaf82/%EB%AC%B4%EB%8A%AC%EC%82%B0%ED%98%B8%EC%88%98.jpg",
        "price": 20000,
        "category_class": "분양해요",
        "status_class": "분양대기",
        "addr": {
            "id": 5,
            "sido": "서울특별시",
            "sigungu": "광진구"
        },
        "posting_addr": 893570,
        "user": {
            "pk": 1,
            "username": "plantinum_test"
        }
    }
]
```



### 잎팔이 검색

- 선택한 카테고리/식물이름/시도/시군구에 해당하는 모든 글 조회
- page, limit으로 구분
- page는 게시글들 중 몇 페이지, limit은 한 페이지에 보이는 게시글 수를 의미
- 식물이름은 `무늬`만 입력해도 `무늬관음죽`, `무늬산호수` 등을 모두 포함하여 조회
- 시도는 반드시 일치하는 값만 조회
- 시군구는 `용인시`를 검색한다면 `용인시`, `용인시 처인구` `용인시 기흥구` 등을 모두 포함하여 조회
- 검색어/시도/시군구 하나만 선택 가능, 중복선택 가능
- 값이 있는 것만 키와 값을 담아 요청
- 최신순으로 조회

- GET
- URL

```
http://127.0.0.1:8000/api/v1/leaf82/search
```

```
# 예시
http://127.0.0.1:8000/api/v1/leaf82/search?page=1&limit=3&category_class=분양해요&sido=서울특별시&sigungu=광진구&plantname=무늬산호수
```

- Params

| Key            | Type   | Description         | Mandatory  | Example    |
| -------------- | ------ | ------------------- | ---------- | ---------- |
| plantname      | String | 식물이름(검색어)    |            | 무늬산호수 |
| sido           | String | 시도                |            | 서울특별시 |
| sigungu        | String | 시군구              |            | 광진구     |
| category_class | String | 분양해요/분양받아요 | O          |            |
| page           | Int    |                     | 1이 기본값 | 1          |
| limit          | Int    | 20으로 고정         | O          | 20         |

- Response

```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "pk": 1,
            "plantname": "무늬산호수",
            "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/images/leaf82/%EB%AC%B4%EB%8A%AC%EC%82%B0%ED%98%B8%EC%88%98.jpg",
            "price": 20000,
            "category_class": "분양해요",
            "status_class": "분양대기",
            "addr": {
                "id": 5,
                "sido": "서울특별시",
                "sigungu": "광진구"
            },
            "posting_addr": 893570,
            "user": {
                "pk": 1,
                "username": "plantinum_test"
            }
        }
    ]
}
```



### 잎팔이 글 상세 조회

- 특정 잎팔이 글 pk에 해당하는 글 상세 조회
- GET
- URL

```
http://127.0.0.1:8000/api/v1/leaf82/{username}/{posting_addr}/
```

- Request Parameters

| Name         | Type   | Description                                                  | Mandatory | Example        |
| ------------ | ------ | ------------------------------------------------------------ | --------- | -------------- |
| username     | String | 유저id                                                       | O         | plantinum_test |
| posting_addr | Int    | 잎팔이 글 작성시 부여되는 랜덤 값<br />한 유저 내에서 중복되지 않음 | O         | 893570         |

- Response

```
{
    "id": 1,
    "user": {
        "pk": 1,
        "username": "plantinum_test",
        "nickname": "플랜티넘테스트",
        "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/static/profile.jpg"
    },
    "addr": {
        "id": 5,
        "sido": "서울특별시",
        "sigungu": "광진구"
    },
    "plantname": "무늬산호수",
    "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/images/leaf82/%EB%AC%B4%EB%8A%AC%EC%82%B0%ED%98%B8%EC%88%98.jpg",
    "created_at": "2022-08-13T21:41:46.909668",
    "content": "광진구에서 직거래원해요~",
    "price": 20000,
    "category_class": "분양해요",
    "status_class": "분양대기",
    "posting_addr": 893570
}
```



### 잎팔이 글 수정

- 로그인 사용자 - 토큰 사용

- PUT
- URL

```
http://127.0.0.1:8000/api/v1/leaf82/{username}/{posting_addr}/
```

- Request Parameters

| Name         | Type   | Description                                                  | Mandatory | Example        |
| ------------ | ------ | ------------------------------------------------------------ | --------- | -------------- |
| username     | String | 유저id                                                       | O         | plantinum_test |
| posting_addr | Int    | 잎팔이 글 작성시 부여되는 랜덤 값<br />한 유저 내에서 중복되지 않음 | O         | 893570         |

- Body

| Key            | Type   | Description                                | Mandatory | Example    |
| -------------- | ------ | ------------------------------------------ | --------- | ---------- |
| sido           | String | 시도                                       | O         | 서울특별시 |
| sigungu        | String | 시군구                                     | O         | 종로구     |
| plantname      | String | 식물이름                                   | O         | 무늬산호수 |
| content        | Text   | 내용                                       | O         | 채팅주세요 |
| price          | Int    | 가격                                       | O         | 15000      |
| category_class | String | 분양해요/분양받아요                        | O         | 분양해요   |
| status_class   | String | 분양대기/분양완료/분양예약<br />default=분양대기 | O         | 분양완료  |
| photo          | ImageFile | 새로운 사진/기존사진/기본사진 | O        ||

- Response

```
# 정상 수정
{
    "id": 1,
    "user": {
        "pk": 1,
        "username": "plantinum_test",
        "nickname": "플랜티넘테스트",
        "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/static/profile.jpg"
    },
    "addr": {
        "id": 1,
        "sido": "서울특별시",
        "sigungu": "종로구"
    },
    "plantname": "무늬산호수",
    "photo": "https://plantinum.s3.ap-northeast-2.amazonaws.com/images/leaf82/%EB%AC%B4%EB%8A%AC%EC%82%B0%ED%98%B8%EC%88%98.jpg",
    "created_at": "2022-08-13T21:41:46.909668",
    "content": "채팅주세요",
    "price": 15000,
    "category_class": "분양해요",
    "status_class": "분양완료",
    "posting_addr": 893570
}
```

```
# 없는 게시글
{
    "detail": "찾을 수 없습니다."
}
```

```
# 다른 사람의 게시글
{
    "detail": "잘못된 접근입니다."
}
```



### 잎팔이 글 삭제

- 로그인 사용자 - 토큰 사용

- DELETE
- URL

```
http://127.0.0.1:8000/api/v1/leaf82/{username}/{posting_addr}/
```

- Request Parameters

| Name         | Type   | Description                                                  | Mandatory | Example |
| ------------ | ------ | ------------------------------------------------------------ | --------- | ------- |
| username     | String | 유저id                                                       | O         | test1   |
| posting_addr | Int    | 잎팔이 글 작성시 부여되는 랜덤 값<br />한 유저 내에서 중복되지 않음 | O         | 426408  |

- Response

```
# 정상 삭제
{
    "detail": "게시글이 삭제되었습니다."
}
```

```
# 없는 게시글
{
    "detail": "찾을 수 없습니다."
}
```

```
# 다른 사람의 게시글
{
    "detail": "잘못된 접근입니다."
}
```





