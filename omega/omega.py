import struct
import sys
from unicorn import Uc, UC_ARCH_X86, UC_MODE_64, UC_HOOK_CODE, UcError
from unicorn.x86_const import (
    UC_X86_REG_RCX, UC_X86_REG_RSP, UC_X86_REG_RSI,
    UC_X86_REG_EDI, UC_X86_REG_EFLAGS, UC_X86_REG_EAX,
)

BASE = 0x140000000
LEN = 0x36  # required flag length (checked in main before calling the VM)

# (virtual_addr, file_offset, size) for every loadable section, taken
# from the PE section table (objdump -h omega.exe).
SECTIONS = [
    (0x1000, 0x400, 0x7000),   # .text
    (0x8000, 0x7400, 0x200),   # .data
    (0x9000, 0x7600, 0x1000),  # .rdata (jump table, strings, VM bytecode, S-boxes)
    (0xa000, 0x8600, 0x600),   # .pdata
    (0xb000, 0x8c00, 0x600),   # .xdata
    (0xd000, 0x9200, 0x800),   # .idata
    (0xe000, 0x9a00, 0x200),   # .CRT
    (0xf000, 0x9c00, 0x200),   # .tls
    (0x10000, 0x9e00, 0x200),  # .reloc
]

VERIFY_FUNC = 0x140001480          # the VM entry point, called from main
CMP_HOOK_ADDR = 0x140001576        # cmovne eax, r9d inside the EQ-check handler


def make_uc(data):
    uc = Uc(UC_ARCH_X86, UC_MODE_64)
    uc.mem_map(BASE, 0x20000)
    for va, ro, sz in SECTIONS:
        uc.mem_write(BASE + va, data[ro:ro + sz])
    uc.mem_map(0x150000, 0x10000)          # stack
    uc.mem_map(0x999000, 0x1000)           # fake return address page
    uc.mem_write(0x999000, b"\xc3")        # ret
    return uc


def emu_verify(data, flag_bytes):
    uc = make_uc(data)
    sp = 0x150000 + 0x8000
    flag_addr = BASE + 0x18000
    uc.mem_write(flag_addr, flag_bytes + b"\x00")
    uc.reg_write(UC_X86_REG_RCX, flag_addr)

    log = []  # (computed_value, target_value, matched)

    def hook_cmov(uc, address, size, user_data):
        edi = uc.reg_read(UC_X86_REG_EDI)
        rsi = uc.reg_read(UC_X86_REG_RSI)
        rsp = uc.reg_read(UC_X86_REG_RSP)
        val_a = struct.unpack("<i", uc.mem_read(rsp + rsi * 4 + 0x40, 4))[0]
        zf = (uc.reg_read(UC_X86_REG_EFLAGS) >> 6) & 1
        log.append((val_a, edi, zf))

    uc.hook_add(UC_HOOK_CODE, hook_cmov, begin=CMP_HOOK_ADDR, end=CMP_HOOK_ADDR)

    sp -= 8
    uc.mem_write(sp, struct.pack("<Q", 0x999000))
    uc.reg_write(UC_X86_REG_RSP, sp)
    try:
        uc.emu_start(VERIFY_FUNC, 0x999000, timeout=0, count=2_000_000)
    except UcError:
        pass
    return uc.reg_read(UC_X86_REG_EAX) & 0xFFFFFFFF, log


def solve(path):
    data = open(path, "rb").read()
    flag = bytearray(b"0" * LEN)
    for pos in range(LEN):
        for c in range(32, 127):
            flag[pos] = c
            _, log = emu_verify(data, bytes(flag))
            if len(log) > pos and log[pos][2] == 1:  # ZF=1  this position matched
                break
        else:
            raise RuntimeError(f"no candidate matched position {pos}")
    eax, log = emu_verify(data, bytes(flag))
    assert eax == 1 and all(m for _, _, m in log), "solved flag failed final check"
    return bytes(flag).decode()


if __name__ == "__main__":
    exe = sys.argv[1] if len(sys.argv) > 1 else "omega.exe"
    print(solve(exe))
