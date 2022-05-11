# cipher text = (plaintext)^e mod n
# C = P^e mod n
# n = p * q (bilangan prima)

plaintext = 12
e = 65537

p = 17
q = 23

cipher = pow(plaintext, e, (p * q))
print(cipher)