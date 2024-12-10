# 프로그램 실행
from login import login_user
from signup import register_user


def doLoginSignup():
    print("1: 회원가입")
    print("2: 로그인")
    choice = input("선택하세요(1 또는 2): ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    else:
        print("잘못된 입력입니다. 프로그램을 종료합니다.")