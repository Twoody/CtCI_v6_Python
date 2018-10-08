'''
	Q1.6: String Compression
		Implement a method to perform basic string compression
		using the counts of repeated characters. For exmaple, the 
		string `aabcccccaaa` would become `a2b1c5a3`. If the 
		compressed string would not become smaller than the original
		string, your method should return the original string.

	Thoughts:
		Does the string contain numbers?
			If so, tens of numbers would be an issue.
			For example if we take in `111111111111` (12 ones),
			we would return `112`, which would confuse our decompressor...
		If we have a small size, we can create a new string and increment quickly.
		If we have a larger size that does not allow us to fit in memory,
		we could write to file each chunk that we go through.
			For example input `aaabbbbccccc` would read a,a,a and write `a3` to file.
			We would then go back and read in `b,b,b,b` and write `b4 to file...

'''
import os

def compressToFile(bigFile, dest=""):
	if dest == "":
		dest = bigFile + '.sml'
	with open(dest, 'w') as outfile, open(bigFile, 'r', encoding='utf-8') as infile:
		for line in infile:
			line = line.replace('\n', '').replace('\r', '').replace(' ', '')
			nline = compress(line)
			outfile.write(nline)
	return dest

def compress(bigS):
	if bigS == "":
		return ""
	smallS  = ""
	curr    = bigS[0]
	currcnt = 1
	for i in range(1, len(bigS)):
		if curr == bigS[i]:
			currcnt += 1
		else:
			smallS += curr + str(currcnt)
			curr = bigS[i]
			currcnt = 1
	smallS += curr + str(currcnt)
	return smallS

def q6():
	assert compress("a") == "a1"
	assert compress("") == ""
	assert compress("aabb") == "a2b2"
	assert compress("aaaaaqqqqwwwwww") == "a5q4w6"
	tFile = "__testFile.txt"
	createTestFile(tFile)
	dest = compressToFile(tFile)
	isvalid = validateNewTestFile(dest)
	assert isvalid == True
	print("PASSED ALL TESTS FOR Q6")
	return True
	
def validateNewTestFile(tFile):
	with open(tFile, 'r') as infile:
		for line in infile:
			compareTo = ""
			for i in range(97, 123):
				compareTo += chr(i) + "199"
			if line != compareTo:
				return False
	return True

def createTestFile(tFile):
	tFile = "__testFile.txt"
	if os.path.isfile(tFile):
		return True
	with open(tFile, 'w') as outfile:
		for i in range(97,123):
			nline = ""
			for j in range(0,199):
				nline += chr(i)
			outfile.write(nline + '\n')
	return True

if __name__ == "__main__":
	q6()
