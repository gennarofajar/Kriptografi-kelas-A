'''
euler totient --- phi atau φ

phi(n) = menghitung ada berapa bilangan yang 
relatif prima terhadap n

definisi relatif prima:
    gcd (..., n) = 1

salah satu sifat totient:
    phi(p * q) = phi(p) * phi(q)
'''

# di soal sudah diberi tahu bahwa p dan q adalah prima
p = 857504083339712752489993810777
q = 1029224947942998075080348647219

# jumlah phi dari p dan q adalah masing masing dikurangi 1
# karena selalu relatif prima kecuali di bilangan sendiri
n = (p - 1) * (q - 1)

print(n)
