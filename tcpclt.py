#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Ejemplo de cliente TCP que utiliza servidor socket
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

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(params)

messages = [
	b'1clave1|valor1',	# Agregar dato
	b'1clave2|valor2',	# Agregar dato
	b'0clave1',		# Petición de clave
	b'clave1',		# No conforme con su primer byte
	b'0cle3',		# Clave no existente
	b'1clavevalor',		# Agregar no correctamente formateado
	b'1clave|valor|',	# Agregar no correctamente formateado
	b'1clave1|valor42',	# Actualización de dato
	b'0clave1',		# Deberíamos tener el nuevo dato
]

for m in messages:
	print("Envío de un mensaje %s" % m)
	s.send(m)
	data = s.recv(BUFFER_SIZE)
	if len(data) == 0:
		print('\tSin respuesta')
	elif data[0] == 48:
		print('\tMensaje no correctamente transmitido')
	elif data[0] == 49:
		print('\tDato transmitido al servidor')
	else:
		print('\tDato recuperado del servidor : %s' % data)
s.close()
