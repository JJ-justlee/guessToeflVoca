import psycopg2
import bcrypt
import encDecModule
from psycopg2 import connect

from config.keyConfig import user, dbPassword, host, saltKey

simpleEnDecrypt = encDecModule.SimpleEnDecrypt(saltKey)

#데이터베이스 연결 정보
DB_CONFIG = {
    'dbname': 'postgres', #데이터베이스 이름
    'user': simpleEnDecrypt.decrypt(user), #사용자 이름
    'password': simpleEnDecrypt.decrypt(dbPassword), #비밀번호
    'host': simpleEnDecrypt.decrypt(host), #호스트 주소
    'port': 5432 #포트 번호
}

#데이터 베이스 연결 함수
def connect_db():
    """데이터베이스에 연결합니다."""
    try:
        conn = psycopg2.connect(**DB_CONFIG) #psycopg2 is one of libraries for postgresql(Database Management)
        return conn
    except Exception as e:
        print("데이터베이스 연결 실패", e)
        return None

