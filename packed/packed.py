def rc4_keystream(key, n):
    S = list(range(256)); j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) & 0xff
        S[i], S[j] = S[j], S[i]
    i = j = 0
    out = bytearray()
    for _ in range(n):
        i = (i + 1) & 0xff
        j = (j + S[i]) & 0xff
        S[i], S[j] = S[j], S[i]
        out.append(S[(S[i] + S[j]) & 0xff])
    return bytes(out)

target = bytes.fromhex("9dfdf517b11122fb66d5d273ec6b09cdae3c601cc0ca983f0cc7367510947428633ddded51d6ba16b0fc9784")
key = b"Super_Secret_K9y"

ks = rc4_keystream(key, len(target))
print(bytes(a ^ b for a, b in zip(target, ks)).decode())
