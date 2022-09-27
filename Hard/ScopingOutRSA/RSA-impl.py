"""
Quick Hacky Implementation of RSA
"""

#P = 13
#Q = 17

# 1024 bit key 
P = 2347 # 170007611163882156467583070449223838584656753148867131633512190380283049593667937234054209916788376143894984910718820080485130228317492395177494053588704733242066260215738749826985323020318900966858054745093276666701971181051299894745771442097807356197274229456637808451705389506462483315002459525647
Q = 2693 # 481643715591972638598218313298174701613643321254523884689569786332541775926781293302556117738302307356981609721753075739005830996780920022755885174107599088199228946117515541982018885577402946246815718309298010594221374531947169982607824253065171036917904012166986458504590468987728792073331236197449

N   = P * Q #
phi = (P-1) * (Q-1) #

e = 257

e2 = e
d = 73721
top1 = phi
top2 = phi
'''
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
'''

print("RSA Components")
print("P: ", P)
print("Q: ", Q)
print("N: ", N)
print("phi: ", phi)
print("e: ", e)
print("d: ", d)


# Bob 
def encrypt(plaintext: str, publicKey):
    e = publicKey[0]
    N = publicKey[1]
    # str bytes hex int -> pow encrypt -> pow decrypt -> int hex bytes str
    # ciphertext = b""
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        if len(plaintext[i:i+2]) < 2:
            text = plaintext[i:i+2] + '0'*(2 - len(plaintext[i:i+2]))
        else:
            text = plaintext[i:i+2]
        s_i = int(text.encode().hex(), 16)
        # print(s_i)
        cipher = pow(s_i, e, N)
        ciphertext += str(cipher) + '-'
    return str(ciphertext)

    '''
    for i in range(0, len(plaintext)):
        ch = plaintext[i]
        ch = ord(ch)
        
        # message - m e s s a g e 
        if ch < 100:
            ch = "0" + str(ch)
        else:
            ch = str(ch)


        # 1231 234 5435 235 345 6356 
        ciphertext += ch

    # "066097"
    m = int(ciphertext)
    c = pow(m,e,N)

    return str(c)
    '''

        
plaintext = "image dimensions"
ciphertext = encrypt(plaintext, [e,N])

print("Ciphertext:", ciphertext)


def decrypt(ciphertext, privateKey):
    d = privateKey[0]
    N = privateKey[1]
    message = ''
    c = ''
    #for i in range(0, len(ciphertext)):
    for i in ciphertext.split('-'):
        try: c = int(i)
        except: c = '0'
        # print(c)
        try: decrypted = str(pow(c, d, N))
        except: return message
        # print("dec", decrypted)
        decrypted = hex(int(decrypted))[2:]
        m = bytes.fromhex(decrypted).decode()
        # print(m, end = '')
        message += str(m)
        c = ''
    return message

    '''
    if len(str(m)) % 3 != 0:
        m = "0" + str(m)
    
    m = str(m)
    # Ba -> 066097
    message = ""

    for i in range(0, len(m), 3):
        ch = m[i:i+3]
        ch = chr(int(ch))

        message += ch

    return message
    '''


message = decrypt(ciphertext, [d,N])
print("Message: ", message)
