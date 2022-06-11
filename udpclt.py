#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Ejemplo de cliente UDP que utiliza el servidor realizado con socket
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
#s.connect(params)

messages = [
	b'1clave1|valor1',	# Agregar dato
	b'1clave2|valor2',	# Agregar dato
	b'0clave1',		# Ne debería funcionar
	b'clave1',		# No conforme con su primer byte
	b'1clavevalor',		# Agregar no correctamente formateado
	b'1clave|valor|',	# Agregar no correctamente formateado
	b'1clave1|valor42',	# Actualización de dato
	b'2clave1',		# Eliminar el dato
	b'3',			# Apagado del servidor
]

for m in messages:
	print("Envío de un mensaje %s" % m)
	#s.send(m)
	s.sendto(m, params)
#s.close()
