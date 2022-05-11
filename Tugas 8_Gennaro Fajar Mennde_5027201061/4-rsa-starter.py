'''
Private key (d)
- invers dari e modulo (p - 1)(q - 1)
- d * e === 1 (mod (p - 1)(q - 1))

e adalah angka random
p & q adalah angka prima
'''

p = 857504083339712752489993810777
q = 1029224947942998075080348647219

# ngitung (p - 1)(q - 1)
hasil = (p - 1) * (q - 1)

e = 65537

# e^-1 mod hasil
d = pow(e, -1, hasil)
print(d)