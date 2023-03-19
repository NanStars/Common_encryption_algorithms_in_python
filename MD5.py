import hashlib


def encrypt_to_md5(str_encrypt):
    """字符串加密到md5"""
    hashlib.md5(str_encrypt.encode("utf8"))
    m = hashlib.md5(str_encrypt.encode("utf8"))
    return m.hexdigest()


if __name__ == '__main__':
    print(encrypt_to_md5('123456'))