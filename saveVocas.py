from modules.db import connect_db
import chatgptToeflVoca


def saveToeflVocaInDB(voca, meaning, ex_sample, is_correct):
    conn = connect_db()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        cur.execute("SELECT email  FROM users WHERE id = %s", (1,))
        email = cur.fetchone()

        if email:  # email이 존재할 경우
            email_value = email[0]  #email 값을 가져옴 (tuple에서 값 추출)

            #another_table에 email 값 삽입
            cur.execute(
                "INSERT INTO voca (user_id, email, voca, meaning, ex_sample, is_correct) VALUES (%s, %s, %s, %s, %s, %s)",
                ('test', email,voca, meaning, ex_sample, is_correct)
            )

        conn.commit()

    except Exception as e:
        print(f"오류 발생: {e}")
        conn.rollback()  # 오류 발생 시 롤백

    finally:
        # 연결 종료
        cur.close()
        conn.close()

