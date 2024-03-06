import bcrypt


def hash_password(password, salt=None):
    if salt is None:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return salt, hashed_password
    else:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8'))
        return hashed_password


def get_password_hash(password):
    salt, hashed_password = hash_password(password)
    return salt, hashed_password


def gen_password_hash(password, salt):
    hashed_password = hash_password(password, salt)
    return hashed_password


# 验证密码是否正确
def verify_password(password, hashed_password, salt):
    input_hashed_password = gen_password_hash(password, salt)
    if input_hashed_password == hashed_password.encode('utf-8'):
        return True
    else:
        return False


if __name__ == '__main__':
    print(hash_password("12345678"))
