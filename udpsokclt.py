#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Ejemplo de cliente UDP que utiliza el servidor realizado con socketserver
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

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

messages = [
	b'1clave1|valor1\n',	# Agregar dato
	b'1clave2|valor2\n',	# Agregar dato
	b'0clave1\n',		# Puede mantener el funcionamiento
	b'clave1\n',		# No conforme con su primer byte
	b'1clavevalor\n',	# Agregar no correctamente formateado
	b'1clave|valor|\n',	# Agregar no correctamente formateado
	b'1clave1|valor42\n',	# Actualización de dato
	b'2clave1\n',		# No se implementa más
]

for m in messages:
	print("Envío de un mensaje %s" % m)
	s.sendto(m, params)
	data = s.recv(BUFFER_SIZE)
	if len(data) == 0:
		print('\tSin respuesta')
	elif data[0] == 48:
		print('\tMensaje no correctamente transmitido')
	elif data[0] == 49:
		print('\tDato transmitido al servidor')
	else:
		print('\tDato recuperado del servidor : %s' % data)
