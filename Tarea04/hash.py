#!/usr/bin/python
# -*- coding: utf-8 -*-

from hashlib import md5, sha1
from datetime import datetime
from sys import argv

md5 = md5(argv[1]).hexdigest()
sha1 = sha1(argv[1]).hexdigest()

time = datetime.now()
hour = str(time.hour) + ':' + str(time.minute) + ':' + str(time.second)

if __name__ == '__main__':
	print hour	
	print md5
	print sha1


