#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Ejemplo de servidor UDP que utiliza socket
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


import socket


params = ('127.0.0.1', 8808)
BUFFER_SIZE = 1024 # default

datos = {}

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#, socket.SOCK_STREAM)
s.bind(params)
# Las líneas siguientes no tienen sentido en UDP:
#s.listan(1)
#conn, addr = s.accept()
#print('Conexión aceptada: %s' % str(addr))

while True:
	#data = conn.recv(BUFFER_SIZE)
	data, addr = s.recvfrom(BUFFER_SIZE)
	print('Conexión recibida: %s' % str(addr))
	print('Dato recibido: %s' % data)
	if data[0] == 49:
		d = data[1:].split(b'|')
		if len(d) != 2:
			print('\tDato no conforme')
			continue
		k, v = d[0], d[1]
		datos[k] = v
		print('\tDato actualizado')
	elif data[0] == 50:
		d = data[1:]
		if d in datos.keys():
			del datos[d]
	elif data[0] == 51:
		break
	else:
		print('\tDato no conforme %s' % data[0])
#conn.close()
