'''
	Tanner.L.Woody@gmail.com
	20180918

	Problem:
		Given a smaller string `s` and a bigger string `b`,
		design an algorithm to find all permuations of the 
		shorter string within the longer one.
		Print the location of each permutation.

	Example1:
		s = 'foo'
		b = 'foo bar baz'
		mf(s,b)
		>>>Index `0`

	Example2:
		s = 'foo'
		b = 'foo bar baz oof ofo'
		mf(s,b)
		>>>Index `0`:	foo
		   Index `12`:	oof
		   Index `16`:	ofo

	Example3:
		s = 'abbc'
		b = 'cbabadcbbabbcbabaabccbabc'
		mf(s,b)
		>>>Index `0`: cbbac
		...

	Solution:
		First thoughts are to remove all characters that are not 
		the characters that are found in our smaller string.
'''
def stringToArr(s):
	return list(s)

def attempt1(s, b):
	#s is substring
	#b is bigger string
	#Walk through b until found char in s
	matches = []
	for i in range(0, len(b)-len(s)+1):
		currletter = b[i]
		if currletter in s:
			temp_s = stringToArr(s)
			for j in range(i, i+len(s)):
				if b[j] in temp_s:
					temp_s.remove(b[j])
				else:
					break;
			if len(temp_s) == 0:
				matches.append( (i, b[i:i+len(s)]) )
	return matches

def main():
	s 	 = 'foo'
	b 	 = 'foo bar baz oof ofo'
	res = attempt1(s,b)
	print('TEST1:\n\t`'+s+'`\n\t`' +b+ '`')
	for i in res:
		print ('\tINDEX `'+ str(i[0]) +'`:\t`' + str(i[1]) + '`')
	
	s 	 = 'abbc'
	b   = 'cbabadcbbabbcbabaabccbabc'
	print('\nTEST2:\n\t`'+s+'`\n\t`' +b+ '`')
	res = attempt1(s,b)
	for i in res:
		print ('\tINDEX `'+ str(i[0]) +'`:\t`' + str(i[1]) + '`')

if __name__ == "__main__":
	main()
