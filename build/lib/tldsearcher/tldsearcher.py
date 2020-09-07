#!/usr/bin/python3

# KNOWN ISSUES AND BUGS | HELP WELCOME
# When scanning, and the x.y domain being tried is not responding, and the user uses CTRL-C, the system throws an error like "handled exception during gaierror exception"
# Proxy scanning is slow and always returns 0 when using .get_status_code(), or None when using .get()

# TODO
# ====
# Implement proxy use for requests
# Fix 'During handling of the above exception, another exception occurred:' error when using CTRL-C during a scan.

import socket
import argparse
import time
import sys
import tlds
# from proxy_requests import ProxyRequests
from __init__ import __version__
version = __version__

list = 'listOfDomains'
targets=[]# Targets to scan
listOfDomains=[]# TLD list to check
result=[]# (Positive) results
args=''
verbose = False
proxy = False
attempts=0# Number of TLDs attempts to find
pos=[]# list of positive results
lastTry=''# Last tried TLD
domainCategory=0# for -domain-category menu
continueDomain = ''# --domain-continue tld
continueDomainIndice=0#--domain-continue tld indice in tlds.py
outputFile=''
max_scans=-1


def main():
		if len(sys.argv) <= 1:
			print('Use -h for help')
		else:
			setTarget()

			scan()

			printer()

			if args.output:
				output(f'''====================
Target domain: {args.target}
====================
Atempted:----------: {attempts}
Positive results:--: {len(pos)}
Last Attempt: -----: {lastTry}''')
				if len(pos)>=1:
					output(f'''========================
[+] Positive Results [+]
========================
{"".join(pos)}''')
				else:
					print('''========================
[-] No Results Found [-]
========================''')


def output(line):
	original_stdout = sys.stdout
	with open(args.output, 'a') as o:
		sys.stdout = o
		print(line)
		sys.stdout = original_stdout

def printer():
	print(f'''====================
Target domain: {args.target}
====================
Atempted:----------: {attempts}
Positive results:--: {len(pos)}
Last Attempt: -----: {lastTry}''')
	if len(pos)>=1:
		print(f'''========================
[+] Positive Results [+]
========================
{"".join(pos)}''')
	else:
		print('''========================
[-] No Results Found [-]
========================''')

def scan():
	print(f'''  _______ _      _____   _____                     _
 |__   __| |    |  __ \ / ____|                   | |
    | |  | |    | |  | | (___   ___  __ _ _ __ ___| |__   ___ _ __
    | |  | |    | |  | |\___ \ / _ \/ _` | '__/ __| '_ \ / _ \ '__|
    | |  | |____| |__| |____) |  __/ (_| | | | (__| | | |  __/ |
    |_|  |______|_____/|_____/ \___|\__,_|_|  \___|_| |_|\___|_|
    https://www.github.com/plague-anon/TLDSearcher/wiki
========================================
[+] Starting TLDSearcher at {time.strftime('%H:%M:%S')} [+]
----------------------------------------
''')# Ascii banner and time started
	if args.output:
		output(f'''  _______ _      _____   _____                     _
 |__   __| |    |  __ \ / ____|                   | |
    | |  | |    | |  | | (___   ___  __ _ _ __ ___| |__   ___ _ __
    | |  | |    | |  | |\___ \ / _ \/ _` | '__/ __| '_ \ / _ \ '__|
    | |  | |____| |__| |____) |  __/ (_| | | | (__| | | |  __/ |
    |_|  |______|_____/|_____/ \___|\__,_|_|  \___|_| |_|\___|_|
    https://www.github.com/plague-anon/TLDSearcher/wiki
========================================
[+] Starting TLDSearcher at {time.strftime('%H:%M:%S')} [+]
----------------------------------------''')# Ascii banner and time started
	for target in targets:
		for tld in listOfDomains:
			url = f'{target}{tld}'
			if verbose:
				print(f'Trying: {url}')

			global lastTry
			lastTry=tld

			global attempts
			attempts += 1

			global max_scans
			if max_scans >=1:
				max_scans -= 1
			elif max_scans == 0:
				sys.exit(printer())

			# if args.proxy:
			# 	proxyScan(url)
			# else:
			# 	normalScan(url, target, tld)
			normalScan(url, target, tld)

# TODO: Too slow and retuns 0
# def proxyScan(url):
# 	try:
# 		r = ProxyRequests(f'https://{url}')
# 		print(r.get_status_code())
# 	except Exception as e:
# 		print(e)


def normalScan(url, target, tld):

	try:
		response = socket.gethostbyname_ex(url)
		if response[2]:
			if verbose:
				print(f'  [+] Found that {target} has TLD of {tld} || hostname: {response[0]} | IP: {response[2]}')
			else:
				print(f'[+] Found that {target} has TLD of {tld}')
			pos.append(f'{target}{tld}\n')
	except socket.gaierror: # No response from server
			if verbose:
				print(f'  [-] No match found for {target}{tld}')

def sortTLD(tld):
# Takes in list of domains from either user -d TLDs or -dF FILE
# If from -d flag, user must use , between tlds they wish to scan
# NOTE: the preceeding . is not needed as this function enters it if missing
	if str(tld).find(','): # tld is from user -d input
		tldsplitlist = str(tld).split(',',-1) # split user input at , (type is list)
		for tld in tldsplitlist:
			if tld[0]!='.':
				listOfDomains.append(f'.{tld}')
			else:
				listOfDomains.append(tld)
	else:
		for t in tld:
			print(t)
			sys.exit()
		# TODO: sanitise input from user specified file

def setVars():
	global listOfDomains
	global outputFile
	global max_scans

	if args.max_scans:
		if int(args.max_scans) >= 1:
			max_scans = int(args.max_scans)-1
		else:
			sys.exit(print('You must give a number >= 1 for --max_scans'))
	#
	# if args.proxy:
	# 	global proxy
	# 	proxy = True

	if args.verbose:
		global verbose
		verbose=True

	if args.domain:
		sortTLD(args.domain)
	elif args.domainFile:
		domainInputFile = open((domainFile), 'r').readlines()
		for d in domainInputFile:
			sortTLD(domainInputFile)
	elif args.domainContinue:
		global continueDomain
		adc = args.domainContinue
		if adc[0] == '.':
			continueDomain = adc
		else:
			continueDomain = f'.{adc}'
		continueDomainIndice = tlds.tldList['all'].index(continueDomain)
		listOfDomains = tlds.tldList['all'][continueDomainIndice:len(tlds.tldList['all'])]
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
		listOfDomains = tlds.getTlds(int(domainChoice))
	else:
		listOfDomains = tlds.tldList['all']

	if args.output:
		outputFile = args.output


def setArgs():
	parser = argparse.ArgumentParser(description='Search for active Top Level Domains(TLD\'s) for domain names.',usage='%(prog)s {[-t <TARGET>] [-tF <TARGET_FILE>]} {[-d com,co.uk,.net] [-dF <DOMAIN_FILE>] [-dC] [-dc <DOMAIN_TO_CONTINUE_FROM>]} [-o <OUTPUT_FILE_NAME>] [-v] ')
	parser.add_argument('-t', '--target', help='targets domain name to scan for listOfDomains', action='store')
	parser.add_argument('-tF', '--targetFile', help='Supply a targets file', action='store')
	parser.add_argument('--max_scans', help='Maximum number of TLDs to scan', action='store')
	parser.add_argument('-o', '--output', help='File to output results into', action='store')
	#parser.add_argument('-p', '--proxy', help='Use proxies for requests (VERY SLOW!)', action='store_true')
	parser.add_argument('-v', '--verbose', help='Verbose output mode', action='store_true')
	parser.add_argument('--version', help='Display version information', action='version', version='%(prog)s ' + version)

	group = parser.add_mutually_exclusive_group()
	group.add_argument('-d', '--domain', help='list of domains to scan. (com,ua,nz,de)', action='store')
	group.add_argument('-dC', '--domainCategory', help='Scan specific TLD categories', action='store_true')
	group.add_argument('-dc', '--domainContinue', help='Continue scanning all domains, starting from last attempt "..."', action='store')
	group.add_argument('-dF', '--domainFile', help='List of listOfDomains to scan. (Default = all)', action='store')

	global args
	args = parser.parse_args()

def setTarget():
	global targets
	if args.target:
		targets.append(args.target)
	elif args.targetFile:
		tFile = open(('args.targetFile'), 'r')
		for x in tFile.readlines():
			if checkTarget():
				targets.append(tFile.readlines())

if __name__ == '__main__':
	setArgs()
	setVars()
	main()
