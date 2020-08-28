#!/usr/bin/python3

import socket
import argparse
import time
import sys
import tlds
version = '1.0.5'

list = 'TLDLIST'
targets=[]# Targets to scan
tldList=[]# TLD list to check
result=[]# (Positive) results
args=''
verbose = False
attempts=0# Number of TLDs attempts to find
pos=[]
lastTry=''# Last tried TLD
domainCategory=0

def main():

	if len(sys.argv) <= 1:
		print('Use -h for help')
	else:
		setTarget()

		scan()

		printer()

def printer():
	print(f'''
====================
[/] TLD SEARCHER [\]   by plague
====================
Atempted:----------: {attempts}
Positive results:--: {len(pos)}
Last Attempt: -----: {lastTry}
========================
[+] Positive Results [+]
========================
{"".join(pos)}''')

def scan():
	print(f'''
===================================
Starting TLDScanner at {time.strftime('%H:%M:%S')} [+]
-----------------------------------
''')
	for target in targets:
		for tld in tldList:
			global lastTry
			global attempts
			global posResults
			attempts += 1
			lastTry=tldList[attempts-1]
			if verbose:
				print(f'Trying: {target}{tld}')
			url = f'{target}{tld}'
			try:
				response = socket.gethostbyname_ex(url)
				if response[2]:
					if verbose:
						print(f'  Found that {target} has TLD of {tld} || hostname: {response[0]} | Alias: {response[1]} | IP: {response[2]}')
					else:
						print(f'  Found that {target} has TLD of {tld}')
					pos.append(f'{target}{tld}\n')
					posResults+=1
			except KeyboardInterrupt:
				sys.exit(printer())
			except socket.gaierror: # No response from server
					if verbose:
						print(f'  No match found for {target}{tld}')
			except Exception as e:
				if verbose:
					log = []
					log.append(f'Error: {e}')





def sortTLD(tld):
# Takes in list of domains from either user -d TLDs or -dF FILE
# If from -d flag, user must use , between tlds they wish to scan
# NOTE: the preceeding . is not needed as this function enters it if missing
	if str(tld).find(','): # tld is from user -d input
		tldsplitlist = str(tld).split(',',-1) # split user input at , (type is list)
		for tld in tldsplitlist:
			if tld[0]!='.':
				tldList.append(f'.{tld}')
			else:
				tldList.append(tld)
	else:
		for t in tld:
			print(t)
			sys.exit()
		# TODO: sanitise input from user specified file

def setVars():
	if args.verbose:
		global verbose
		verbose=True

# TODO: Prevent using more than one domain-related flag.
	if args.domain:
		sortTLD(args.domain)
	elif args.domainFile:
		domainInputFile = open((domainFile), 'r').readlines()
		for d in domainInputFile:
			sortTLD(domainInputFile)
	elif args.domainCategory:
		print('''
[1] Countries ---------	(ccTLD | .ua, .nz, .de, .es, .ru, etc)
[2] Original Generic --	(gTLD |  .com, .net, .org, .info, etc.)
[3] Internet ----------	(.io, .tech, .cloud, .network, etc.)
[4] Money and finance -	(.trade, .marketing, .finance, etc.)
[5] Technology -------- (.tech, .app, .systems, .security, etc.)
[6] Professional ------ (.pro, .work, .consulting, .careers, etc.)
[7] Government -------- (.tax, .army, .gov, .mil, .voting, etc.)
[8] All ---------------	(Scans ALL TLDs)
		''')
		print('Select which category you want to search for.')
		domainChoice = input('Type a number and click ENTER: ')
		global tldList
		tldList = tlds.getTlds(int(domainChoice))
	else:
		domainInputFile = open((list), 'r').readlines()
		for x in domainInputFile:
			tldList.append(x.strip('\n'))

def setArgs():
	parser = argparse.ArgumentParser(description='Search for active Top Level Domains(TLD\'s) for domain names.',usage='%(prog)s {[-t <TARGET>] [-tF <TARGETFILE>]} {[-d com,co.uk,.net] [-dF <DOMAINFILE>] [-dC]} [-v] ')
	parser.add_argument('-t', '--targets', help='targets domain name to scan for tldList', action='store')
	parser.add_argument('-tF', '--targetFile', help='Supply a targets file', action='store')
	parser.add_argument('-d', '--domain', help='tldList to scan. (com,ua,nz,de)', action='store')
	parser.add_argument('-dC', '--domainCategory', help='Scan TLD categories', action='store_true')
	parser.add_argument('-dF', '--domainFile', help='List of tldList to scan. (Default = all)', action='store')
	parser.add_argument('-v', '--verbose', help='Verbose output mode', action='store_true')
	parser.add_argument('--version', help='Display version information', action='version', version='%(prog)s ' + version)
	global args
	args = parser.parse_args()

def setTarget():
	if args.targets:
		targets.append(args.targets)
	elif args.targetFile:
		tFile = open(('args.targetFile'), 'r')
		targets.append(tFile.readlines())

if __name__ == '__main__':
	setArgs()
	setVars()
	main()
