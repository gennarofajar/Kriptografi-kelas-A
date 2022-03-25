def gcd(x, y):
    if x < y:
        return gcd(y, x)

    while y != 0:
        (x, y) = (y, x % y)

    print("\n[+] GCD: {}".format(x))
    return x

a = 66528
b = 52920

gcd(a, b)