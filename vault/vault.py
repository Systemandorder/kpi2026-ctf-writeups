
import struct

d = open("vault.exe", "rb").read()
def off(va): return va - 0x140000000 - 0x9000 + 0x7400   # VA -> offset .rdata

T = d[off(0x140009040):][:48]
K = struct.unpack('<4I', d[off(0x140009070):][:16])

M, DELTA = 0xffffffff, 0x9e3779b9

def dec(v0, v1):
    s = (DELTA * 32) & M
    for _ in range(32):
        v1 = (v1 - ((((v0 << 4) ^ (v0 >> 5)) + v0) ^ (s + K[(s >> 11) & 3]))) & M
        s  = (s - DELTA) & M
        v0 = (v0 - ((((v1 << 4) ^ (v1 >> 5)) + v1) ^ (s + K[s & 3]))) & M
    return v0, v1

out = b''.join(struct.pack('<2I', *dec(*struct.unpack('<2I', T[i:i+8])))
               for i in range(0, 48, 8))
print(out[:41].decode())
