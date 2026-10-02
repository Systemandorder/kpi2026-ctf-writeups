N = 0x2250f38be239677f 
# movabs 0x2250f38be239677f,rsi у дизасемблері
e = 65537 
# mov 0x10001,ebx
 
# 7 очікуваних ciphertext-блоків з таблиці .rdata (адреса 0x14000a040),
# кожен  8 байт :
ciphertext_hex_blocks = [
"749478ca9a8c700a",
"1d7c87dc5c81531c",
"690d8bdbe980a01d",
"b093f8b5e3b1f020",
"b983c13110b9aa1f",
"c82554b56d226904",
"0678cb1a3d79640d",
]
ciphertext_blocks = [int.from_bytes(bytes.fromhex(h), "little")
for h in ciphertext_hex_blocks]
 
 
def factor_N(n):
"""Розкласти N на два прості множники. N  всього 61 біт,
 sympy справляється миттєво (на відміну від справжнього RSA,
де N — сотні,тисячі біт і це було б неможливо)."""
from sympy import factorint
f = factorint(n)
primes = list(f.keys())
assert len(primes) == 2, f"очікували рівно 2 прості множники, отримали f,тобто якщо множників більше"
p, q = primes
assert p * q == n# assert УМОВА, ПОВІДОМЛЕННЯ  якщо УМОВА хибна , Python кидає помилку AssertionError з текстом ПОВІДОМЛЕННЯ і зупиняє виконання. Якщо умова істинна йде далі, нічого не виводячи.
return p, q
 
 
def solve():
p, q = factor_N(N)
print(f"N = p * q: p={p}, q={q}")
 
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi) # закритий експонент   RSA
print(f"d = {d}")
 
flag = b"".join(
pow(c, d, N).to_bytes(7, "big") # розшифровка блоку: m = cd mod N
for c in ciphertext_blocks
)
return flag.rstrip(b"\x00") # прибрати нульовий відступ останнього блоку
 
 
if __name__ == "__main__":
print("FLAG:", solve().decode())
