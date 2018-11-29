#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#XML - parser
import sys
import xml.etree.ElementTree as ET
from datetime import datetime


usuarios = []
class Usuario:
    def __init__(self,username,password,uid,gid,gecos,home,shell):
        self.username = username
        self.password = password
        self.uid = uid
        self.gid = gid
        self.gecos = gecos
        self.home = home
        self.shell = shell

    def __str__(self):
        return '%s:%s:%s:%s:%s:%s:%s\n' % (self.username,
                                           self.password,
                                           self.uid,
                                           self.gid,
                                           self.gecos,
                                           self.home,
                                           self.shell)



def printError(msg, exit = False):
    sys.stderr.write('Error:\t%s\n' % msg)
    if exit:
        sys.exit(1)



def lee_xml(archivo_passwd):
    with open(archivo_passwd,'r') as passwd:
        root = ET.fromstring(passwd.read())
        for user in root.findall('user'):
            username = user.find('username').get('value')
            password = user.find('password').get('value')
            uid = user.find('uid').get('value')
            gid = user.find('gid').get('value')
            gecos = user.find('gecos').get('value')
            home = user.find('home').get('value')
            shell = user.find('shell').get('value')
            usuario = Usuario(username,password,uid,gid,gecos,home,shell)
            usuarios.append(usuario)



def escribe_reporte(archivo_reporte):
    with open(archivo_reporte,'w') as output:
        output.write(str(datetime.now()) + '\n')
        map(lambda u: output.write(str(u)),usuarios)



if __name__ == '__main__':
    if len(sys.argv) != 3:
        printError('Indicar archivo a leer y archivo de reporte.', True)
    lee_xml(sys.argv[1])
    escribe_reporte(sys.argv[2])
