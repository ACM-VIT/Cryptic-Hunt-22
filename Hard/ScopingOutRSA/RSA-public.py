"""
Quick Hacky Implementation of RSA
"""
print("Enter the appropriate values for the key: ")
P = int(input("P: "))
Q = int(input("Q: "))

N   = P * Q 
phi = (P-1) * (Q-1) 

# From: https://www.cs.drexel.edu/~jpopyack/IntroCS/HW/RSAWorksheet.html
print("Find an appropriate value for e from: https://www.cs.drexel.edu/~jpopyack/IntroCS/HW/RSAWorksheet.html")
e = int(input("e: ")) 
d = 1 

e2 = e
top1 = phi
top2 = phi

# Extended Euclidean GCD
while e2 != 1:
    k = top1 // e2
    # 192 // 5 = 38

    oldTop1 = top1
    oldTop2 = top2

    top1 = e2
    top2 = d

    e2 = oldTop1 - k * e2
    d  = oldTop2 - k * d

    if d < 0:
        d = d % phi

# str bytes hex int -> pow encrypt -> pow decrypt -> int hex bytes str

def decrypt(ciphertext, privateKey):
    d = privateKey[0]
    N = privateKey[1]
    message = ''
    c = ''
    for i in ciphertext.split(' '):
        try: c = int(i)
        except: c = '0'
        try: decrypted = str(pow(c, d, N))
        except: return message
        decrypted = hex(int(decrypted))[2:]
        m = bytes.fromhex(decrypted).decode()
        message += str(m)
        c = ''
    return message

print("RSA Components")
print("P: ", P)
print("Q: ", Q)
print("N: ", N)
print("phi: ", phi)
print("e: ", e)
print("d: ", d)

ciphertext = "1732163 5171910 3568538 1422380 386379 5598431 3074781 386379 2061289 4911475 4409697 4949774 4409697 5983717 5388075 386379 2795238 2205174 2226983 5640197 902015 4934468 4292385 1478935 2264601 1324739 2226983 1393793 3337111 3104134 2268001 2016417 2205174 328177 2183508 5952038 2264601 1676206 5791545 4135654 81129 4154723 6147504 4949774 1697492 563424 4934468 369692 1324739 2226983 934447 369692 328177 2016417 1393793 2368657 1123377 5732711 2875758 3947269 2609679 3574230 3556270 3337111 4866124 902015 3702975 2226983 4135654 81129 4154723 6147504 4949774 1697492 2724199 5226818 913600 1422380 386379 2016417 6230403 386379 5640197 902015 4934468 2724910 1393793 4071090 302140 5179421 112000 1817104 369692 913600 955368 5732711 2005727 1422380 1274623 5179421 5736222 6147504 4949774 4409697 3702975 2692430"
message = decrypt(ciphertext, [d,N])

print("Message: ", message)
