import requests

ciphertext_hex = requests.get('http://aes.cryptohack.org/symmetry/encrypt_flag/').json()
ciphertext = ciphertext_hex['ciphertext']
print(ciphertext)


iv = ciphertext[:16*2]
print(iv)

ciphertext = ciphertext[32:]
print(ciphertext)


plaintext_hex = requests.get('http://aes.cryptohack.org/symmetry/encrypt/{}/{}'.format(ciphertext, iv)).json()
plaintext = plaintext_hex['ciphertext']
print(plaintext)
flag = bytes.fromhex(plaintext)
print(flag)

# crypto{0fb_15_5ymm37r1c4l_!!!11!}