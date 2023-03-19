import hashlib


def encrypt_to_sha(str_encrypt, type=1):
    if type == 1:
        # sha 1
        hash = hashlib.sha1(str_encrypt.encode("utf8"))
    elif type == 256:
        # sha 256
        hash = hashlib.sha256(str_encrypt.encode("utf8"))
    elif type == 512:
        # sha 512
        hash = hashlib.sha512(str_encrypt.encode("utf8"))
    else:
        return None
    hash.update(str_encrypt.encode("utf8"))
    value = hash.hexdigest()
    return value


if __name__ == '__main__':
    str_encrypt = "123456"
    print(encrypt_to_sha(str_encrypt))
