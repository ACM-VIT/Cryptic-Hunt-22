# Small Wiener

* **Category:** Hard
* **Mode:** Online
* **Author:** Chirag
* **Points:** TBD

## Specifications

* **Entry point:** Clue is hidden in the description and the code snippet to understand the encryption is given.
* **Reward:** The decrypted text.

## Description

Harsh's girlfriend wants to send a secret text to Harsh. She encrypts the message with Harsh's RSA public key which is { e: 601363702787219970639669573943, N: 701590986585091644415556358149 }.  
Here's how she encrypts the secret text:
```python3
with open("secret.txt", "r") as f:
    a = f.read().strip()

N = 701590986585091644415556358149
e = 601363702787219970639669573943

m = int(a.encode('utf-8').hex(), 16)
c = pow(m, e, N)

print(c)
```
She gets the output as: 552571332635354884887823434083 and sends it to Harsh via an insecure channel. You have successfully intercepted her message and want to know what was the secret text.  
Looking at the public key exponent (e) which is very large, You know that **Harsh will surely have a small d** (private key exponent).

Can you find out what the secret text was?

## Solution 1 - Bruteforce

1. Since private key exponent is very small, you can perform a bruteforce attack and check if decrypted text is valid utf-8 to get the answer.

## Solution 2 - Wiener's attack
Read this article to understand the solution - https://sagi.io/crypto-classics-wieners-rsa-attack/ 

1. Find continued fraction expansion of the rational number with numerator as public key exponent (e) and denominator as N (modulus) i.e e / N.
```python3
N = 701590986585091644415556358149
e = 601363702787219970639669573943

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

cf = continued_fraction(e, N)
```

2. Find convergents of this continued fraction.
```python3
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

convergents = convergents(cf)
```

3. Find the right k / d among the convergents. (Read the article to understand what k & d is.)  
```python3
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
        d = (b * b) - (4 * a * c)

        # If the quadratic equation has real roots
        if d > 0:
            r1 = (-b + math.sqrt(abs(d))) / (2 * a)
            r2 = (-b - math.sqrt(abs(d))) / (2 * a)

            # If roots are integers and none of them is 0
            if r1 == int(r1) and r2 == int(r2) and r1 != 0 and r2 != 0:
                p = int(r1)
                q = int(r2) 
                break             
```

4. You now have the prime factors of N (p & q), You can use them to find phi(N) (Euler's Totient function) and then find private key exponent (d) using phi(N).
```python3
phi_N = (p - 1) * (q - 1)
d = pow(e, -1, phi_N)
```

5. Decrypt the message using the private key.
```python3
M = pow(ct, d, N)
temp = hex(M)[2:]
if len(temp) % 2 != 0:
    temp = "0" + temp

pt = bytes.fromhex(temp).decode('utf-8')
print(f"Decrypted secret text is: {pt}")
```

6. You get the output as `Decrypted plain text is: h4R5H4v1n45H`

## Hints:

 - Hint 1 (Cost = TBD): https://en.wikipedia.org/wiki/Wiener%27s_attack
 - Hint 2 (Cost = TBD): https://sagi.io/crypto-classics-wieners-rsa-attack/
