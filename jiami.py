import base64
from operator import xor
from Crypto.Cipher import AES

def add_to_16(s):
        while len(s) % 16 != 0:
            s += '\0'
        return str.encode(s)  # 返回bytes

def aes_jiami(text):
    # 密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
    key = 'LeslieCheungKwok'
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(text))), encoding='utf8').replace('\n', '')
    return encrypted_text

def xor_jiami(s,key):
    xor_s = ''
    for i in s:
        xor_s += chr(ord(i) ^ key)
    return xor_s


if __name__=='__main__':
    sc = 'payload'
    with open('./aes-xor.txt','w') as f:
        f.write(aes_jiami(xor_jiami(sc,35)))
    




