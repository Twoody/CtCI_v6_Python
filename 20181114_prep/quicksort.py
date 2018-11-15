'''
quicksort works off of controlling two indexs.
The first index is 0.
The second index is equal to the last element of the last.
For example:
	i = 0
	j = len(arr)-1
We then choose a `pivot` such that the pivot is the middle element in our array.

Once these values are set, we iterate through the area.
Array iteration compares the arr[i] element to our pivot.value.
	if arr[i] > pivot.value:
		i+=1

Similarly, we iterate j backwards, comparing to pivot:
	if arr[j] > pivot:
		j-=1

Once we have both i and j stagnat, swap them.

Repeat this process until i == j

When i does equal j, we now have a portion of the array sorted
such that that entire portion is less than our first pivot value.

Store this i,j shared indice (alpha)

Now, choose a new pivot.
The pivot should be in the middle.
The pivot should be between our previous shared indice, alpha.
Set j equal to alpha.
set i equal to zero.
Repeat the process.

At the point that we are down to an array of 3 or less elements,
we can just use insertion sort, and now set a new variable, beta.
beta will tell us to not go back and visit pass this point.
That is, for the rest of the program, i>beta

Repeat this process until alpha and i are the length of the array
'''

def quicksort(arr):
	n = len(arr)
	if n<2:
		return arr
	pivot   = arr[n//2]
	less    = [i for i in arr[1:] if i<=pivot]
	greater = [i for i in arr[1:] if i>pivot]
	return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == "__main__":
	arr = [12,124,4,12,2,224,42,12,3,4,55,33,22]
	print(quicksort(arr))
