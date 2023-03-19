import binascii
from pyDes import des, CBC, PAD_PKCS5


# 加密过程
def des_encrypt(secret_key, value):
    """
    secret_key:key
    value:加密值
    """
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(value, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


# 解密过程
def des_decrypt(secret_key, value):
    """
   secret_key:key
   value:加密值
   """
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(value), padmode=PAD_PKCS5)
    return de


if __name__ == '__main__':
    secret_str = des_encrypt('12345678', 'hello')
    print(secret_str)

    clear_str = des_decrypt('12345678', secret_str)
    print(clear_str)
