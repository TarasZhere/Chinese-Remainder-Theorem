# Taras Zherebetskyy
# The program calculates the CRT (Chinese Remainder theorem)
# it returns None if there is not answer

def multInvers(m, x):  
    a = [0, 1]
    q = [None, None]
    r = [m, x]
    i = 1
    
    while r[i] > 1:
        i += 1
        r.append(r[i - 2] % r[i - 1])
        q.append(r[i - 2] // r[i - 1])
        a.append((a[i-2] - q[i] * a[i - 1]) % m)

    if r[i] == 1: return a[i]
    else: return None

def mult(m):
    num = 1
    for i in m:
        num *= i
    return num

def CRT(r, m):
    N = mult(m)
    A = []
    X = 0

    for i in m:
        b = int(N / i)
        inverse = multInvers(i, b)

        if inverse is None: 
            return inverse

        A.append((b * inverse) % N)
    
    for i,j in zip(A, r):
        X += (i * j)
    return X % N

def askdata():
    r = []
    m = []

    print("\nEnter the remainders like that: r1 r2 ... ri\nRemainders: ", end="")
    r = [int(i) for i in input().split()]

    print("\nEnter the moduli like that: m1 m2 ... mi\nModuli: ", end="")
    m = [int(i) for i in input().split()]
    return r, m

r, m = askdata()

print(f"\nThe solution of {r} mod {m} is:", CRT(r, m))
