# QTside6

- .ui 파일 .py 로 변환
```
 pyside6-uic [파일명.ui] -o [원하는파일명.py]
```


- 리소스 존재할 때 (이미지 삽입)

```
pyside6-rcc [파일명.ui] -o [원하는파일명_rc.py]
```


- External Tool 설정
```
1. [경로]\venv\Scripts\pyside6-uic.exe
2. $FileDir$\[파일명].ui -o $FileDir$\[파일명].py

```
> open 어쩌고 두번째 체크박스 해제

> rcc 도 같은 방법 사용