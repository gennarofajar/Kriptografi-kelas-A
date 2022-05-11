'''
https://en.wikipedia.org/wiki/General_number_field_sieve

https://math.stackexchange.com/questions/2437665/how-to-find-prime-factors-of-big-numbers-made-up-of-big-prime-factors

http://factordb.com #i surrender

https://www.youtube.com/watch?v=tKTNVmnW_4w 
-> n = x^2 - y^2, x = sqrt(n + Y^2)

p = (x + y)
q = (x - y)
'''

N = 510143758735509025530880200653196460532653147

from math import sqrt

primes = []

def isPrime(x):
	global primes
	if x in primes:
		return True
	
	for divisor in primes:
		if divisor > sqrt(x):
            # kalau divisor > sqrt (x) maka kelebihan angkanya
			break
	
		if x % divisor == 0:
			# X is non-prime
			return False
	
	primes.append(x)
	return True
	
def factorize(x):
	primeFactors = []
	divisor = 2
	while x > 1:
		if isPrime(divisor):
			if x % divisor == 0:
				x = x / divisor
				primeFactors.append(divisor)
			else:
				divisor += 1
		else:
			divisor += 1	
	return primeFactors
	
factors = factorize(N)

print(factors)

# hasil: 19704762736204164635843, 25889363174021185185929