"""Poor implementation - will unecessarly recur again for already found values - For example: fibo(5) will again
compute for, for example fibo(3) and fibo(4) will aslo compute for fibo(3). So time complexity will be very poor"""
def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# Change this value for a different result
#nterms = 50 #This code just hangs or too slow to compute beyond few terms
#for i in range(nterms):
#	print(recur_fibo(i))

#Memoization - This is a good technique where a cache will store any previously computed values.
#Time complexity of O(n)
memo = {}
def memo_fibo(n):
	if n in memo:
		return n
	elif n == 1:
		value = 1
	elif n == 2:
		value = 2
	elif n > 2:
		value = memo_fibo(n-1) + memo_fibo(n-2)
	memo[n] = value
	return value

for i in range(1,51):
	print(memo_fibo(i))
print("\n\n\n=================calling lru cache ================= \n\n\n")
from functools import lru_cache
@lru_cache(maxsize=1000)
def fibo_lru(n):
	if n == 1:
		return n
	elif n == 2:
		return 1
	elif n > 2:
		return fibo_lru(n-1) + fibo_lru(n-2)

for i in range(1,51):
	print(fibo_lru(i))