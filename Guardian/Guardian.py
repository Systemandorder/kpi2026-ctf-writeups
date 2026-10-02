TE = bytes.fromhex("5660e07db7b9a246f7bc4fdd4c2ebdaa890fbd8ce3d420a263d7f45ec5a999abb1920089bd977241c1fd")
KE = bytes.fromhex("7d59cb341f65802c")

T = bytes(b ^ 110 for b in TE)   # Dec(): XOR 110
K = bytes(b ^ 110 for b in KE)

seed = 0xC0FFEE
s = list(range(256))
for i in range(255, 0, -1):
    seed = (seed * 1103515245 + 12345) & 0x7fffffff
    j = seed % (i + 1)
    s[i], s[j] = s[j], s[i]
inv = {v: k for k, v in enumerate(s)}

flag = bytes((inv[T[i] ^ K[i % 8]] - i) & 255 for i in range(42))
print(flag.decode())
