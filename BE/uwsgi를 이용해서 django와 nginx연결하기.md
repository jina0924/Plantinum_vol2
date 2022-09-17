# DJANGO와 NGINX 그리고 Vue.js연결하는 법 (feat. UWSGI)
<br>

## 개요
 - Django는 Spring과 달리 바로 nginx에 올릴 수 없다.
 - 그래서 uwsgi라는 것을 이용하여 연결을 해주어야 한다.
 - 기본적인 방법과 겪은 오류를 해결하는 과정을 담았다. 
 #### 가정
- python 3.9.1
- linux 환경 
- nginx 설치
---
<br>
<br>
<br>


 ## Django
 - 장고 기본 프로젝트 만들기
 

 1. 가상환경 설치 및 활성화
 ```console
    python -m venv venv
    source venv/bin/activate
 ```
 2. 가상환경 안에 장고 설치 및 실행
 ```console
    pip install django
    django-admin.py startproject back
    
    # 프로젝트 위치로 이동
    cd backend

    # 파일이 이미 있는 경우 패키지 설치_ git 등
    pip install -r requirements.txt

    # 서버 실행
    python manage.py runserver 
 ```
* 기본적으로 장고의 포트는 8000번이다 바꾸고 싶으면 runserver 뒤 포트번호를 입력하면 된다. 

<details>
<summary>migration</summary>
<div markdown="1">

- 없어도 돌아가기는 한다
- 해당 프로젝트 폴더 안에서

```console
    python manage.py migration
```
- settings.py에서 데이터베이스 명시가 필요하긴 하다.

</div>
</details>

<br>

<details>
<summary>install 오류</summary>
<div markdown="1">

- pip 업데이트 확인 필요
- wheel 이나 다른것 설치가 필요하다.
```console
    pip install wheel
```
- settings.py에서 데이터베이스 명시가 필요하긴 하다.

- mysql-client 오류 시 해당 설치 후 다시 설치하면 잘된다.
```console
    sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

</div>
</details>

---

<br>
<br>
<br>

 ## USWGI
 - 장고가 잘 된다면 다음은 uwsgi다.
 1. uwsgi 설치
 ```console
    pip install uwsgi
```
2. 명령어가 길다. 그러므로 폴더를 만들어 관리해준다. manage.py가 있는 폴더로 간 후
```console
    # .config/uwsgi 만들어줌
    mkdir .config
    cd .config
    mkdir uwsgi
```

3. [프로젝트 이름].ini 만들고 추가 저의 경우 back.ini

```bash
[uwsgi]
#프로젝트 폴더 절대 경로
chdir = /home/ubuntu/back
#절대 경로 안 wsgi파일 경로
module = back.wsgi:application
#가상환경 경로
home = /home/ubuntu/venv/
 
uid = ubuntu
gid = ubuntu
 
 #1
#http = :8000
 #2
socket = /tmp/back.sock
chmod-socket = 666
chown-socket = ubuntu:ubuntu

 
enable-threads = true
master = true
vacuum = true
pidfile = /tmp/mysite.pid
logto = /var/log/uwsgi/back/@(exec://date "+%%Y-%%m-%%d").log
log-reopen = true


```
- logto는 오류 내용을 확인하기 위한 로그 파일이다. 


- #1은 확인을 위한것 #2는 본격적으로 nginx와 소켓으로 연결을 하기 위한것이다.
- #2 방법 사용


<details>
<summary>모듈이 존재하지 않아요!</summary>
<div markdown="1">

- 몇시간을 고민하도록 한 문제이다.
- uswgi를 실행했는데 모듈이 없는 문제이다.
```
    module = back.wsgi:application
```
- 이 부분에서 manage.py 가 있는 경로가 아닌 다른 파일에 wsgi.py가 있다 그 폴더 명을 써줘야한다.

</div>
</details>

---

<br>
<br>
<br>

## Vue.js연결

1. 주의!!! vue에서 장고 연결을 할때 localhost로 쓰면 안된다. 
2. 서버명 정확히 명시 해 줄 것
3. vue에서 build파일 만들기
```console
    npm run build
```
4. /var/www/html/ 에 만들어진 dist 파일 업로드


---

<br>
<br>
<br>

## NGINX 연결
1. nginx가 이미 설치 되었다는 가정하에 config파일을 바꿔준다. 
    - 이 과정에서 새로 바꿔서 만들지 않고 기존 default를 바꿔줄 것이다.

2. 경로로 가서 default 수정
```
    cd /etc/nginx/sites-available
    sudo vi default
```
3. default 수정

```bash
server {
        listen 80 default_server;
        listen [::]:80 default_server;
        server_name _;

        #vue저장한 위치
        root /var/www/html/dist;
        index index.html index.htm;

        location / {
                try_files $uri $uri/ /index.html;

        }

        #uswgi_pass는 back의 uwsgi설정 파일에서 정해준 소켓 위치
        location /api/ {
            uwsgi_pass     unix:///tmp/back.sock;
            include                uwsgi_params;
        }
}

```

4. 데몬 리로드, 및 리스타트를 해줌

```
    sudo systemctl daemon-reload
    sudo systemctl restart uwsgi nginx
```

<br>

위 과정을 하고 백엔드 서버를 킨 후 사이트 접속 시 잘 돌아간다!

# 배포 성공!!


 