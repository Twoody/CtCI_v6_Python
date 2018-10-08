"""
	Tanner.L.Woody@gmail.com
	20180918

	Problem:
		A ransom note can be formed by cutting words out of a 
		magazine to form a new sentence.
		How would you figure out if a ransom note (represented 
		as a string) can be formed from a given magazine (string)?

	Thoughts:
		Make an array of all words in magazine, `magWords`.
		Make an array of ransom message, `note`.
		Init hashtable, `mHash`.

		Optimizing resources:
			Most optimal is to have a note of size n fit into a 
			   magWord of size n, too.
			The second most optimal is to have note of size n fit
					into a magWord of size n+1.
			And So on and so forth.

		But is the best use of our resources also the best
			algorithm?
		
		Example1:
			magWords = "A long full article dedicated to my"
				+ " programs, interviews, and future jobs "
				+ " is nothing without the stamp of approval"
				+ " given to me by my wife. She means a lot to"
				+ " me (more than money)  and I like having her"
				+ " happy, content, and in bed before midnight."
			note = "give me the money by midnight"

"""
import re

def canMakeNote(note, magWords):
	mArr = re.split("[^a-zA-Z0-9]", magWords)
	nArr = re.split("[^a-zA-Z0-9]", note)
	#hTbl = {} #key:value >>> index:(mWord, nWord)
	for search in nArr:
		if search in mArr:
			#Direct match in the array
			mArr.remove(search)
			nArr.remove(search)
			#hTble[search] = search
		else:
			#Look up the items one at a time
			for item in mArr:
				if search in item:
					mArr.remove(item)
					nArr.remove(search)
					#hTble[item] = search
	if nArr == []:
		return True
	else:
		print (", ".join(nArr))
		for j in mArr:
			print ("\t" + j)
		return False

def main():
	magWords = "A long full article dedicated to my" 
	magWords += " programs, interviews, and future jobs " 
	magWords += " is nothing without the stamp of approval"
	magWords += " given to me by my wife. She means a lot to"
	magWords += " me (more than money)  and I like having her"
	magWords += " happy, content, and in bed before midnight."
	note = "give me the money by midnight"
	if(canMakeNote(note, magWords)):
		print("CAN MAKE NOTE FROM MAGAZINE")
	else:
		print("CANNOT MAKE NOTE FROM MAGAZINE")

if __name__ == "__main__":
	main()
