import hashlib


def md5(md5_str):
    m = hashlib.md5()
    if isinstance(md5_str, str):
        m.update(md5_str.encode('utf8'))
    else:
        m.update(md5_str)
    return m.hexdigest()