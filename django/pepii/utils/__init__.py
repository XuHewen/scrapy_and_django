import hashlib


def md5(string):
    m = hashlib.md5()
    if type(string) == str:
        m.update(string)
        return m.hexdigest()
    else:
        m.update(string.encode('utf-8'))
        return m.hexdigest()
