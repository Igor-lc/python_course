from sys import argv
import hashlib

# Задаем незашифрованный пароль.
raw_password = 'password'
# Кодируем "сырой" пароль, чтобы воспользоваться md5.
raw_password = raw_password.encode()
# Получаем шифр-объект.
hash_password = hashlib.md5(raw_password)
# Получаем зашифрованный пароль.
hash_password = hash_password.hexdigest()
print(hash_password)  # 5f4dcc3b5aa765d61d8327deb882cf99


hash_password = 'c8b667f4e6953d59b6ae9b9659772333'
raw_pass = argv[1].encode()

hash_pass = hashlib.md5((raw_pass))
hash_pass = hash_pass.hexdigest()
if hash_pass == hash_password:
    print("Доступ открыт")
else:
    print("Доступ закрыт")
