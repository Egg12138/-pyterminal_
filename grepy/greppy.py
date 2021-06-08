#-*-coding=utf-8-*-
#Author Aydenegg

"""
Copy a grep tool in python
"""

import argparse
#import getpass


import re

parser = argparse.ArgumentParser(description='grep tool in py')
parser.add_argument('f',
		type=str,
		help='THe file where you wanna the grep works')
parser.add_argument('pattern',
		 type=str,
		 help='The target pattern(REGEX) you wanna search in the file')

parser.add_argument('--m',
		 dest='mode',
		 action='store',
		 choices={'print', 'count', 'ver'},
		 default='print',
		 help='''[MOD] TO Count the times your pattern appears
		 		 print   print all fit lines.
				 count   return the number of the lines with your patter
				 ver     print lines including not your pattern''')
#A new way to receive the mode, unlike the UNIX-style: -c -n ... 


args = parser.parse_args()



def dealer(src, tar, mod):
	"""
	Match...
	"""
	#TODO RegexMatching
	f = open(src, 'r')
	for line in f.readlines():
		
	if mod == 'print':
		pass
	elif mod == 'count':
		pass		
		

	f.close()


if __name__ == '__main__':
	args = parser.parse_args()
	pattern = args.pattern
	file = args.f 
	mod = args.mode
	print(f"{pattern=}, {file=}, {mod=}")
	dealer(file, pattern, mod)
'''
user = getpass.getuser()
passwd = getpass.getpass()
print(f"{passwd=}")
def loginer(name):
	count = 5
	while count > 0:
		enter = input(f'Password for {name}:')
		if enter != passwd:
			count -= 1
			continue
		else:
			return True
if loginer(user):
	print('Got it')
else:
	print('YOu cannot work as a root')



'''

