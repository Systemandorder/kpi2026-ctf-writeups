MASK = 0xffffffff

def f(c, key):
    edx = c & 0xff
    ecx = edx | key
    eax = edx & key
    edi = (eax ^ 1) & MASK
    edi = edi & 1
    ebp = (eax ^ 0xfffffffe) & MASK
    edi = (ebp + edi * 2) & MASK
    edx = (edx ^ key) & MASK
    edx = edx & eax
    edx = (ecx + edx * 2) & MASK
    edx = (edx + edi) & MASK
    eax = (-eax) & MASK
    ebp = ecx & eax
    eax = (eax ^ ecx) & MASK
    ebp = (eax + ebp * 2) & MASK
    ebp = ebp & 0x7c
    ebp = (ebp + ebp) & MASK
    eax = (edx ^ 0x7c) & MASK
    eax = eax & ebp
    edx = (edx ^ ebp) & MASK
    edx = (edx ^ 0x7c) & MASK
    edx = (edx + eax * 2) & MASK
    edx = edx | 0x35
    eax = ecx & edi
    ecx = (ecx ^ edi) & MASK
    eax = (ecx + eax * 2) & MASK
    eax = (eax ^ 0x7c) & MASK
    eax = (eax + ebp) & MASK
    eax = eax & 0x35
    edx = (edx - eax) & MASK
    return edx & 0xff

table = [0xd2,0xee,0x86,0x0e,0x3d,0x60,0x9d,0x9b,0xa4,0x27,0x1f,0x87,0xf9,0x8d,0x59,0x58, 0x09,0xda,0xcc,0xf0,0x0b,0x35,0x8f,0xf2,0xe0,0x6a,0x1f,0x21,0xa6,0x96,0x1a,0x7b, 0x0e,0xc3,0xf9,0xb2,0x1d,0x16,0x2f,0xe3,0x94] 

flag_bytes = [] for i, target in enumerate(table):
                         key = (0x2f * i) & MASK 
                         candidates = [c for c in range(256) if f(c, key) == target]          


                        flag_bytes.append(candidates[0]) 
                        print(''.join(chr(v) for v in flag_bytes))
