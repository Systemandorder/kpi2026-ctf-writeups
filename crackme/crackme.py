TARGET_HEX = "aeefaae34d2fc9425c7df85f36fe93b18d61e9c6278400155c5a7f345518f76ca1630642236b9f9d79"
 
def ror8(x, n):
x &= 0xff
n %= 8
return ((x >> n) | (x << (8 - n))) & 0xff
 
def inverse_transform(r, i):
v = ror8(r ^ 0xC3, 5)
return (v ^ ((i * 17) & 0xff)) & 0xff
 
def main():
target = bytes.fromhex(TARGET_HEX)
flag = bytes(inverse_transform(r, i) for i, r in enumerate(target))
print(flag.decode())
 
if __name__ == "__main__":
main()





