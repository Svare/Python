#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv, stderr, exit
from datetime import datetime
from hashlib import md5, sha1
import xml.etree.ElementTree as ET

class Host:
	
	def __init__(self, ip, status, port22, honeypot, domain_name):
	
		self.ip = ip
		self.status = status
		self.port22 = port22
		self.honeypot = honeypot
		self.domain_name = domain_name


	def __str__(self):
		domains = reduce(lambda x,y: x + ' ' + y, self.domain_name)
		return '%s,%s,%s,%s,%s\n' % (self.ip, self.status, self.port22, self.honeypot, domains)

def print_error(msg, exit = False):
	stderr.write('Error:\t%s\n' % msg)
	if exit:
		exit(1)

def read_xml(xml_file, hosts):

	on = 0				# Hosts Prendidos
	off = 0				# Hosts Apagados
	open_22 = 0			# Hosts con puerto 22 abierto
	open_53 = 0			# Hosts con puerto 53 abierto
	open_80 = 0			# Hosts con puerto 80 abierto
	open_443 = 0		# Hosts con puerto 443 abierto
	domain_name = 0		# Hosts con nombre de dominio
	apache = 0			# Hosts con servidor Apache
	honeypot = 0		# Hosts que son Honeypots
	nginx = 0			# Hosts con servidores Nginx
	other = 0			# Hosts con otro tipo de servicio

	with open(xml_file,'r') as net_scan:

		root = ET.fromstring(net_scan.read())
		
		for host in root.findall('host'):

			if host.find('status').get('state') == 'up':
				on += 1
			else:
				off += 1

			try:

				ports = host.find('ports').findall('port')

				for port in ports:
					if port.get('portid') == "22":

						if port.find('state').get('state') == 'open':
							open_22 +=1

					elif port.get('portid') == "53":

						if port.find('state').get('state') == 'open':
							open_53 +=1

					elif port.get('portid') == "80":
						
						try:

							if port.find('service').get('product').upper().__contains__('APACHE'):
								apache += 1
							elif port.find('service').get('product').upper().__contains__('DIONAEA'):
								honeypot += 1
							elif port.find('service').get('product').upper().__contains__('NGINX'):
								nginx += 1
							elif len(port.find('service').get('product')) > 0:
								other += 1

						except AttributeError:
							''' Si se atrapa una excepcion aqui quiere decir que a pesar de tener
								una etiqueta llamada puerto en dicha etiqueta no tenemos los 
								atributos que requerimos, entonces simplemente ignoramos la excepcion '''
							pass

						if port.find('state').get('state') == 'open':
							open_80 +=1

					elif port.get('portid') == "443":
		
						if port.find('state').get('state') == 'open':
							open_443 +=1

			except AttributeError:
				''' Si tenemos una excepcion aqui quiere decir que no tenemos una
					etiqueta ports por lo tanto no podemos obtener informacion sobre
					los puertos del host y simplemente ignoramos la excepcion '''
				pass

			try:
				host_ip = host.find('address').get('addr')
			except AttributeError:
				host_ip = 'unknown'

			try:
				host_status = host.find('status').get('state')
			except AttributeError:
				host_status = 'unknown'

			try:
				host_port22_status = host.find('ports').findall('port')[0].find('state').get('state')
			except AttributeError:
				host_port22_status = 'unknown'

			try:
				if host.find('ports').findall('port')[2].find('service').get('product').upper().__contains__('DIONAEA'):
					host_honeypot = 'yes'
				else:
					host_honeypot = 'no'
			except AttributeError:
				host_honeypot = 'unknown'

			try:
				host_domains = []
				for hostname in host.find('hostnames').findall('hostname'):
					host_domains.append(hostname.get('name'))
			except AttributeError:
				host_domains = ['']
			finally:
				if host_domains == []:
					host_domains = ['']
				if host_domains[0] != '':
					domain_name += 1


			new_host = Host(host_ip,
							host_status,
							host_port22_status,
							host_honeypot,
							host_domains)

			hosts.append(new_host)

	return {'Prendidos':on, 'Apagados':off, 'Puerto 22':open_22,
			'Puerto 80':open_80,'Puerto 53':open_53, 'Puerto 443':open_443,
			'Apache':apache, 'Honeypot':honeypot, 'Nginx':nginx, 'Otro':other,
			'Nombre de Dominio':domain_name}

def build_report(report_file, hosts):
    with open(report_file,'w') as output:
    	output.write('ip,host_state,port_22_status,is_honeypot?,domain_name\n')
        map(lambda u: output.write(str(u)), hosts)

def info_report(info):
	print 'Reporte\n'
	print '\tHosts Encendidos: %s' % str(info['Prendidos'])
	print '\tHosts Apagados: %s' % str(info['Apagados'])
	print '\tHosts con Puerto 22 Abierto: %s' % str(info['Puerto 22'])
	print '\tHosts con Puerto 53 Abierto: %s' % str(info['Puerto 53'])
	print '\tHosts con Puerto 80 Abierto: %s' % str(info['Puerto 80'])
	print '\tHosts con Puerto 443 Abierto: %s' % str(info['Puerto 443'])
	print '\tHosts que usan Apache: %s' % str(info['Apache'])
	print '\tHosts que son Honeypots: %s' % str(info['Honeypot'])
	print '\tHosts que usan Nginx: %s' % str(info['Nginx'])
	print '\tHosts que usan Otro Servicio: %s' % str(info['Otro'])
	print '\tHosts con Nombre de Dominio: %s' % str(info['Nombre de Dominio'])
	print '_________________________________________________________________\n'


if __name__ == '__main__':

	# Hashes archivo nmap.xml

	md5 = md5(argv[1]).hexdigest()
	sha1 = sha1(argv[1]).hexdigest()

	# Hora de ejecucion

	time = datetime.now()
	hour = str(time.hour) + ':' + str(time.minute) + ':' + str(time.second)

	hosts = []

	print '\n_________________________________________________________________\n'
	print 'Hora de Ejecucion: ' + hour	
	print 'MD5: ' + md5
	print 'SHA1: ' + sha1
	print '_________________________________________________________________\n'

	# Recibe como primer argumento el archivo xml a parsear y como segundo argumento
	# el archivo donde se va a guardar todo el reporte sobre cada uno de los hosts

	info = read_xml(argv[1], hosts)
	build_report(argv[2], hosts)
	info_report(info)





