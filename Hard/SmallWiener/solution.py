import math  

N = 701590986585091644415556358149
e = 601363702787219970639669573943
ct = 552571332635354884887823434083

def continued_fraction(n, d):
    e = []

    q = n // d
    r = n % d
    e.append(q)

    while r != 0:
        n, d = d, r
        q = n // d
        r = n % d
        e.append(q)

    return e

def convergents(e):
    n = [] 
    d = []

    for i in range(len(e)):
        if i == 0:
            ni = e[i]
            di = 1
        elif i == 1:
            ni = e[i]*e[i-1] + 1
            di = e[i]
        else: # i > 1
            ni = e[i]*n[i-1] + n[i-2]
            di = e[i]*d[i-1] + d[i-2]

        n.append(ni)
        d.append(di)

    return list(zip(n, d))


cf = continued_fraction(e, N)
convergents = convergents(cf)

for i in range(len(convergents)):
    rational = convergents[i]
    numerator = rational[0]
    denominator = rational[1]
    
    k = numerator
    d = denominator

    phi_times_k = ((e * d) - 1)

    # a, b, c represents the coefficients of the Quadratic equation.
    # Read the article - https://sagi.io/crypto-classics-wieners-rsa-attack/ 
    # to know more about this specific quadratic equation.
    a = k
    b = (phi_times_k - k*N) - k
    c = N*k

    if k != 0:
        d = b * b - 4 * a * c

        # If the quadratic equation has real roots
        if d > 0:
            r1 = (-b + math.sqrt(abs(d))) / (2 * a)
            r2 = (-b - math.sqrt(abs(d))) / (2 * a)

            # If roots are integers and none of them is 0
            if r1 == int(r1) and r2 == int(r2) and r1 != 0 and r2 != 0:
                p = int(r1)
                q = int(r2) 
                break

phi_N = (p - 1) * (q - 1)
d = pow(e, -1, phi_N)

M = pow(ct, d, N)
temp = hex(M)[2:]
if len(temp) % 2 != 0:
    temp = "0" + temp

pt = bytes.fromhex(temp).decode('utf-8')
print(f"Decrypted plain text is: {pt}")
