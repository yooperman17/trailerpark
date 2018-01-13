#!/usr/bin/env python

import os
import sys
import subprocess
import datetime

def path(root, subDirectoryOrFile1 = None, subDirectoryOrFile2 = None, subDirectoryOrFile3 = None):
	if subDirectoryOrFile1: root = os.path.join(root, subDirectoryOrFile1)
	if subDirectoryOrFile2: root = os.path.join(root, subDirectoryOrFile2)
	if subDirectoryOrFile3: root = os.path.join(root, subDirectoryOrFile3)
	return root

def currentDirectory():
	return os.path.dirname(os.path.abspath(__file__))
	
def directory(name = None):
	root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
	if name:
		root = path(root, name)
	return root
	
def execute(label, arguments = []):
	print('\n')
	print('---------------------------------------------------')
	print(label + ' ...')
	print('---------------------------------------------------')
	
	process = subprocess.Popen(arguments, stdout = subprocess.PIPE, cwd = currentDirectory() + '/../')
	(output, error) = process.communicate()
	code = process.wait()
	try:
		output = str(output, 'utf-8')
	except:
		output = str(output)
	
	if not output == '':
		print(output)
		print('---------------------------------------------------')
	
def commit(username, password):
	execute('Adding repository', ['git', 'add', '-A'])
	execute('Committing repository', ['git', 'commit',  '-a',  '-m', 'TrailerPark Commit: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ''])
	execute('Pushing repository', ['git', 'push', '--all', 'https://' + username + ':' + password + '@github.com/trailerpark/trailerpark.git'])

def getInput(message):
	try:
		return raw_input(message)
	except:
		return input(message)

def deleteRepository():
	path = directory('repository')
	for item in os.listdir(path):
		itemPath = os.path.join(path, item)
		if os.path.isdir(itemPath):
			for file in os.listdir(itemPath):
				if file.endswith('.zip') or file.endswith('.zip.md5') or file.endswith('.png') or file.endswith('.jpg') or file.endswith('.txt'):
					os.remove(os.path.join(itemPath, file))

if __name__ == '__main__':
	plain = False
	username = None
	password = None
	for i in range(len(sys.argv)):
		if sys.argv[i] == 'plain' or sys.argv[i] == '-plain':
			plain = True
		elif sys.argv[i] == 'username' or sys.argv[i] == '-username':
			i += 1
			username = sys.argv[i]
		elif sys.argv[i] == 'password' or sys.argv[i] == '-password':
			i += 1
			password = sys.argv[i]
	
	if not plain:
		print('***************************************************')
		print('**                  TrailerPark                  **')
		print('***************************************************')
		print('\n')
		
		getInput("Is the VPN connected?")
		getInput("Are you sure the VPN is connected?")
	
	if username == None:
		username = getInput('Git Username: ')
	if password == None:
		password = getInput('Git Password: ')
	
	#deleteRepository()
	commit(username, password)
	
	print('\n')
	if not plain: print('***************************************************')
	print('The repository was updated!')
	if not plain: getInput("Press [Enter] to exit ...")
	if not plain: print('***************************************************')
