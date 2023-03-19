import hmac
import hashlib


def encrypt_to_hmac(key, value, type_=hashlib.md5):
    """
    key:密钥key
    value:待加密的字符串
    type_:hash函数
    return: 加密后的16进制
    """

    mac = hmac.new(key.encode(encoding="utf-8"), value.encode("utf8"), type_)
    return mac.hexdigest()


if __name__ == '__main__':
    key = 'abc'
    value = '123456'
    type = hashlib.md5
    print(encrypt_to_hmac(key, value, type))
