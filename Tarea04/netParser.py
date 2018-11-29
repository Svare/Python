#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv, stderr, exit
from datetime import datetime
from hashlib import md5, sha1
import xml.etree.ElementTree as ET

# Hashes archivo nmap.xml

md5 = md5(argv[1]).hexdigest()
sha1 = sha1(argv[1]).hexdigest()

# Hora de ejecucion

time = datetime.now()
hour = str(time.hour) + ':' + str(time.minute) + ':' + str(time.second)

hosts = []

class Host:
	
	def __init__(self, ):
	
	def __str__(self, ):


def print_error(msg, exit = False):
	stderr.write('Error:\t%s\n' % msg)
	if exit:
		sys.exit(1)

def read_xml(xml_file):
	with open(xml_file,'r') as passwd:
		root = ET.fromstring(passwd.read())
		for user in root.findall('user'):
			username = user.find('username').get('value')
			password = user.find('password').get('value')
			uid = user.find('uid').get('value')
			gid = user.find('gid').get('value')
			usuario = Usuario(username,password,uid,gid,gecos,home,shell)
			usuarios.append(usuario)

if __name__ == '__main__':
	print hour	
	print md5
	print sha1

