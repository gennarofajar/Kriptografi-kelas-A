from datetime import datetime, timedelta
import requests

def print_blk(hex_blks, sz):
   for i in range(0, len(hex_blks), sz):
       print(hex_blks[i:i+sz], ' ', end='')
   print()

def flip(cookie, plain):
    start = plain.find(b'admin=False')
    cookie = bytes.fromhex(cookie)
    iv = [0xff] * 16
    cipher_fake = list(cookie)
    fake = b';admin=True;'
    for i in range(len(fake)):
       cipher_fake[start+i] = plain[start+i] ^ cookie[start+i] ^ fake[i]
       iv[start+i] = plain[start+i] ^ cookie[start+i] ^ fake[i]

    cipher_fake = bytes(cipher_fake).hex()
    iv = bytes(iv).hex()
    return cipher_fake, iv

def request_cookie():
    r = requests.get("http://aes.cryptohack.org/flipping_cookie/get_cookie/")
    return r.json()["cookie"]
    # {"cookie":"27e224a958c206762f62365c32c3e87279d5e2a0c6c2cd1d3a8b91ecedc93cfeb0afaeff6a8c983a46ab44a2fcfd1c36"}

def request_check_admin(cookie, iv):
    r = requests.get("http://aes.cryptohack.org/flipping_cookie/check_admin/{}/{}/".format(cookie, iv))
    return r.json()

expires_at = (datetime.today() + timedelta(days=1)).strftime("%S")
plain = f"admin=False;expiry={expires_at}".encode()
cookie = request_cookie()
cookie, iv = flip(cookie, plain)
print(request_check_admin(cookie, iv))

# crypto{4u7h3n71c4710n_15_3553n714l}