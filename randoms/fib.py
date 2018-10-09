import time
def fib1(n):
	''' return the nth iteration of the fib sequence '''
	''' SUPER SLOW AND BAD'''
	if n==0 or n ==1:
		return n
	return fib1(n-1)+fib1(n-2)

def fib2(n, memoryD):
	print('fib('+str(n)+ ', ' + str(memoryD) +')')
	if n == 0 or n == 1:
		return n
	if n not in memoryD:
		print('\t'+str(n) + ': ' + str(memoryD))
		memoryD[n] = fib2(n-1, memoryD) + fib2(n-2, memoryD)
		print('\t'+str(n) + ': ' + str(memoryD))
	else:
		print('\tIN  MEMORY: ' +str(n))
	return memoryD[n]

def fib1_tests():
	assert fib1(1) == 1
	assert fib1(0) == 0
	assert fib1(2) == 1
	assert fib1(3) == 2
	print( fib2( 4, {} ) )
	print( fib2( 6, {} ) )
	#print( fib2( 38, {} ) )
	#print( fib2( 100, {} ) )
	#print( fib2( 101, {} ) )


if __name__ == "__main__":
	fib1_tests()
