#!/usr/bin/env
'''
Author:
	Tanner Lee Woody 20181016

Purpose:
	Search and replace the given dir if the dir exists;
	The directory name was changed, and we need to make surethe correct path is being imported;

TODO:
	Resolve correct functionality output
'''
import os
	
def searchReplace(f, s1, s2, args=None):
	''' Search and replace file `f` for `s1`, and replacing with `s2` '''
	''' If$ `f` is dir, then iterate through directory doing search replace '''
	'''TODO:
		Resolve correct functionality output'''
	if args is None:
		args = {}
	isverbose = False
	if 'isverbose' in args and args['isverbose'] == True:
		isverbose = True
	if os.path.isdir(f):
		dmap = {}
		for i in os.listdir(f):
			i = f + '/' + i
			if i.endswith('.py') or os.path.isdir(i):
				r = searchReplace(i, s1, s2, args)
			else:
				r = False
			dmap[i] = r
		for i in dmap:
			if dmap[i] == True:
				print('OVERWRITE DONE IN `' + i + '`')
			else:
				print('SEARCH NOT FOUND IN: ' + i + '')
		print()
		return True
	elif os.path.isfile(f):
		if isverbose == True:
			print('WORKING ON:' + f)
		newtext = ''
		willOverwrite = False
		with open(f, 'r') as infile:
			for line in infile:
				if s1 in line:
					willOverwrite = True
					newtext += line.replace(s1, s2)
				else:
					newtext += line
		if willOverwrite == True:
			with open(f, 'w') as outfile:
				outfile.write(newtext)
		if isverbose == True and willOverwrite == True:
			print('searchReplace: WRITING TO FILE `' + str(f) + '`')
		if isverbose == True and willOverwrite == True:
			print('searchReplace: NOT FOUND IN FILE `' + str(f) + '`')
		return True
	elif os.path.exists(f):
		print('WARNING: searchReplace(): CANNOT DETERMINE FILE TYPE')
		return False
	else:
		raise ValueError('ERROR: FILE `' + str(f) + '` CANNOT BE FOUND')

if __name__ =="__main__":
	d   = '/Users/tannerleewoody/Workspace/google/CtCI/2_linkedLists'
	s1  = '/linkedLists/'
	s2  = '/2_linkedLists/'
	print('SEARCHING FOR:  ' + s1)
	print('REPLACING WITH: ' + s2)
	r = searchReplace(d, s1, s2, {'isverbose': True})
	assert r == True
