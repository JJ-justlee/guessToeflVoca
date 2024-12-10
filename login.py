from modules.db import connect_db
import bcrypt

def login_user():
    """사용자가 로그인합니다."""
    email = input("이메일을 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")

    #데이터베이스 연결
    conn = connect_db()
    if conn is None:
        return

    try:
        #데이터베이스에서 사용자 정보 가져오기
        cur = conn.cursor()
        cur.execute("SELECT password_hash FROM users WHERE email = %s", (email,))
        result = cur.fetchone()

        if result is None:
            print("등록되지 않은 이메일입니다.")
        else:
            # 비밀번호 확인
            stored_password = result[0]
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                print("로그인 성공!")
            else:
                print("비밀번호가 틀렸습니다.")

    finally:
        cur.close()
        conn.close()