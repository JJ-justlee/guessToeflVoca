import encDecModule
from config import keyConfig

# 암복호화 클래스 객체를 미리 생성한 키를 받아 생성한다.
simpleEnDecrypt = encDecModule.SimpleEnDecrypt(keyConfig.saltKey)

# 암호화된 액세스키와 시크릿키를 읽어 복호화 한다.
openAiKey = simpleEnDecrypt.decrypt(keyConfig.openAiKey)
user = simpleEnDecrypt.decrypt(keyConfig.user)
dbPassword = simpleEnDecrypt.decrypt(keyConfig.dbPassword)
host = simpleEnDecrypt.decrypt(keyConfig.host)

print(openAiKey)
print(dbPassword)
print(user)
print(host)
