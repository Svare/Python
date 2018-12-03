
import re
from sys import argv

def check(ips, correos):
	with open(ips, 'r') as list_ips, open(correos, 'r') as list_correo:
		ip = [item.strip() for item in list_ips.readlines()]
		correoo = [item.strip() for item in list_correo.readlines()]

		print 'ips\n'

		for i in ip:
			if re.match(ipv4, i) is not None:
				print '%s: Valid' % (i)
			else:
				print '%s: Not Valid' % (i)

		print 'correos\n'

		for c in correoo:
			if re.match(correo, c) is not None:
				print '%s: Valid' % (c)
			else:
				print '%s: Not Valid' % (c)

if __name__ == '__main__':
	ipv4 = r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)[.](25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)[.](25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)[.](25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
	correo = r"[a-zA-Z0-9][a-zA-Z0-9_]*[@][a-zA-Z]+([.][a-zA-Z]){1,}"

	check(argv[1], argv[2])