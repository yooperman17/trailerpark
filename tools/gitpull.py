#!/usr/bin/env python

import os
import subprocess
import datetime

def currentDirectory():
	return os.path.dirname(os.path.abspath(__file__))
	
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
	
def commit():
	execute('Pulling repository', ['git', 'pull'])

def getInput(message):
	try:
		return raw_input(message)
	except:
		return input(message)
	
if __name__ == '__main__':
	print('***************************************************')
	print('**                  TrailerPark                  **')
	print('***************************************************')
	print('\n')
	
	getInput("Is the VPN connected?")
	getInput("Are you sure the VPN is connected?")
	
	commit()
	
	print('\n')
	print('***************************************************')
	print('The repository was pulled!')
	getInput("Press [Enter] to exit ...")
	print('***************************************************')