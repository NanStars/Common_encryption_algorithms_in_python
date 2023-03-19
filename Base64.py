import base64


def encrypt_to_base64(str2):
    """加密"""
    byte_str = base64.b64encode(str2.encode())  # 转化为byte类型
    base64_encrypt_str = byte_str.decode()  # 将字节串转为字符串
    return base64_encrypt_str


def decrypt_to_str(base64_encrypt_str):
    """解密"""
    base64_decrypt = base64_encrypt_str.encode()  # 字符串转为字节串
    str_decrypt = base64.b64decode(base64_decrypt).decode()  # 得到加密的字符串
    return str_decrypt


if __name__ == '__main__':
    str = '123456'
    print(encrypt_to_base64(str))
    print(decrypt_to_str(encrypt_to_base64(str)))
