#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Ejemplo de servidor UDP que usa socketserver
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


import socketserver


params = ('127.0.0.1', 8808)

datos = {}

class ExampleUDPHandler(socketserver.DatagramRequestHandler):
	def handle(self):
		self.data = self.rfile.readline().strip()
		print('Dato recibido: %s' % self.data)
		if self.data[0] == 49:
			d = self.data[1:].split(b'|')
			if len(d) != 2:
				print('\tDato no conforme')
				self.wfile.write(b'0\n')
				return
			k, v = d[0], d[1]
			datos[k] = v
			print('\tDato actualizado')
			self.wfile.write(b'1\n')
		elif self.data[0] == 48:
			d = datos.get(self.data[1:])
			if d is None:
				print('\tNo disponible')
				self.wfile.write(b'0\n')
				return
			print('\tDato devuelto: %s' % d)
			self.wfile.write(d+b'\n')
		else:
			print('Dato no conforme %s' % self.data[0])
			self.wfile.write(b'0\n')

if __name__ == '__main__':
	server = socketserver.UDPServer(params, ExampleUDPHandler)
	server.serve_forever()

