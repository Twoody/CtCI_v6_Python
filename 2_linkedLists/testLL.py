'''
Just a file to test import and a few of the basic principal functions that define
a linked list.
'''
import sys
sys.path.append('/Users/tannerleewoody/Workspace/google/CtCI/linkedLists/')
from LinkedList import LinkedList

def LLPush_1():
	f = LinkedList()
	llc = LinkedList([1])
	f.push(1)
	assert f == llc
	assert f.tail.value == llc.tail.value
	assert f.head.value == llc.head.value

	f.push(2)
	llc = LinkedList([2,1])
	assert f == llc
	assert f.tail.value == llc.tail.value
	assert f.head.value == llc.head.value
	
	f.push([1,2])
	llc = LinkedList([2,1,2,1])
	assert f == llc
	assert f.tail.value == llc.tail.value
	assert f.head.value == llc.head.value
	return True

def LLRemove_3():
	#NOT DONE TEST
	ll			= LinkedList([3,4,8,5,10,2,1])
	temp		= ll.remove(0)
	ll.push(3)
	ll.remove(0)
	if ll.head.value == ll.get(2).value:
		return True
	return True

def LLRemove_2():
	ll = LinkedList([1])
	try:
		ll.remove(9)
		return False
	except ValueError as e:
		return True
def LLRemove_1():
	ll = LinkedList([1,2,3,4])
	ll.remove(0)
	assert ll == LinkedList([2,3,4])
	assert ll.head.value == 2
	assert ll.tail.value == 4

	ll.remove(2)
	assert ll == LinkedList([2,3])
	assert ll.head.value == 2
	assert ll.tail.value == 3

	ll.remove(0)
	ll.remove(0)
	assert ll == LinkedList()
	assert ll == LinkedList([])

	return True

def LLGet_1():
	ll  	= LinkedList([1,2,3])
	node	= ll.get(0)
	nll	= ll.get(0,1)
	assert node.value == 1
	assert nll == LinkedList([1,2])
	return True

def LLLen_1():
	ll = LinkedList([1,2,3])
	if len(ll) == 3:
		return True
	return False

def LLAppend_5():
	ll		= LinkedList()
	ll2	= LinkedList([1,2,3])
	ll.append(1)
	ll.append(2)
	ll.append(3)
	if ll == ll2:
		return True
	else:
		return False
def LLAppend_4():
	ll		= LinkedList()
	ll2	= LinkedList(1)
	ll.append(1)
	if ll == ll2:
		return True
	else:
		return False
def LLAppend_3():
	ll		= LinkedList(1)
	ll2	= LinkedList(1)
	ll.append(1)
	ll2.append(1)
	if ll == ll2:
		return True
	else:
		return False
def LLAppend_2():
	ll		= LinkedList()
	ll2	= LinkedList()
	ll.append(1)
	ll2.append(1)
	if ll == ll2:
		return True
	else:
		return False
def LLAppend_1():
	ll = LinkedList(1)
	ll.append(0)
	ll2 = LinkedList(1)
	ll2.append(0)
	if ll == ll2:
		return True
	else:
		return False
def LLAppend_ValueError():
	ll = LinkedList()
	try:
		ll.append()
	except ValueError as e:
		return True
	return False
def LLInit():
	ll = LinkedList()
	return True

def runtests():
	thisfile = 'testLL.py'
	assert LLInit() == True
	assert LLAppend_ValueError() == True
	assert LLAppend_1() == True
	assert LLAppend_2() == True
	assert LLAppend_3() == True
	assert LLAppend_4() == True
	assert LLAppend_5() == True
	assert str(LinkedList([1,2,3])) == "1 -> 2 -> 3"
	assert str(LinkedList([1,2,3])) == "1 -> 2 -> 3"
	assert LLLen_1() == True
	assert LLGet_1() == True
	assert LLRemove_1() == True
	assert LLRemove_2() == True
	assert LLPush_1() == True
	print(thisfile + ": PASSED ALL TESTS")
	return True

if __name__ == "__main__":
	runtests()
