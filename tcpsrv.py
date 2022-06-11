#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Ejemplo de servidor TCP que utiliza socket
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


params = ('127.0.0.1', 8809)
BUFFER_SIZE = 1024 # default

datos = {}

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(params)
s.listan(1)

conn, addr = s.accept()
print('Conexión aceptada: %s' % str(addr))

while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data:
		break
	print('Dato recibido: %s' % data)
	if data[0] == 49:
		d = data[1:].split(b'|')
		if len(d) != 2:
			print('\tDato no conforme')
			conn.send(b'0')
			continue
		k, v = d[0], d[1]
		datos[k] = v
		print('\tDato actualizado')
		conn.send(b'1')
	elif data[0] == 48:
		d = datos.get(data[1:])
		if d is None:
			print('\tNo disponible')
			conn.send(b'0')
			continue
		print('\tDato devuelto: %s' % d)
		conn.send(d)
	else:
		print('Dato no conforme %s' % data[0])
		conn.send(b'0')
conn.close()
