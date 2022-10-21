import hashlib
def calcular_hash(path):
    h = hashlib.sha1()
    data = open(path,"r",encoding='utf-8')
    d = 0
    while d != b'':
        d = data.read(1024).encode('utf-8')
        h.update(d)
    data.close()
    return h.hexdigest()

    