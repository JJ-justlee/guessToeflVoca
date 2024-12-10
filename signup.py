import bcrypt

from modules.db import connect_db

def register_user():
    """새로운 사용자를 등록합니다."""
    username = input("사용자 이름을 입력하세요: ")
    email = input("이메일을 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")

    #비밀번호를 해시로 변환
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    hashed_password_decode = hashed_password.decode('utf-8')

    #데이터 베이스 연결
    conn = connect_db()
    if conn is None:
       return

    try:
        #데이터베이스에 사용자 정보 저장
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, hashed_password_decode)
        )

        conn.commit()
        print("회원가입이 완료되었습니다!")
    except Exception as e:
        print("회원가입 중 오류 발생:", e)
        conn.rollback()

    finally:
        cur.close()
        conn.close()
