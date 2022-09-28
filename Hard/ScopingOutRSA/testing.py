a = "saharsh"
i = int(a.encode().hex(), 16)
print(i)
 
d = hex(i)[2:]
s = bytes.fromhex(d).decode()
print(s)
