#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Ilustración del funcionamiento de HMAC
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


import hashlib
import hmac

import pickle
from io import BytesIO

import pprint


class SimulatedPipe(object):
	content = BytesIO()
	read = content.read
	write = content.write
	flush = content.flush
	tell = content.tell
	seek = content.seek
	readline = content.readline
simulated = SimulatedPipe()

class SimulatedWriter(object):
	def __init__(self, pipe):
		self.pipe = pipe

	@staticmethod
	def make_digest(key, message):
		"Return a digest for the message."
		return hmac.new(key, message, hashlib.sha1).digest()

	def write(self, key, message):
		pickled = pickle.dumps(message)
		digest = SimulatedWriter.make_digest(key, pickled)
		self.pipe.write(digest + b' ' + bytes(str(len(pickled)), 'utf-8') + b'\n' + pickled)
		self.pipe.flush()
writer = SimulatedWriter(simulated)

class SimulatedReader(object):
	def __init__(self, pipe):
		self.pipe = pipe
		self.position = 0

	def read(self, key):
		position = self.pipe.tell()
		self.pipe.seek(self.position)
		line = self.pipe.readline()
		if not line:
			return
		stored_digest, lenght = line.split(b' ')
		pickled = self.pipe.read(int(lenght))
		self.position = self.pipe.tell()
		self.pipe.seek(position)
		calculated_digest = SimulatedWriter.make_digest(key, pickled)
		#print('Empreinte enregistrée : %s' % stored_digest)
		#print('Empreinte stockée     : %s' % calculated_digest)
		if(stored_digest != calculated_digest):
			print('Datos corruptos o clave incorrecta')
			return
		return pickle.loads(pickled)
reader = SimulatedReader(simulated)

# Test
key = b'mi super clave secreta que nadie conoce'

# Escritura de dos entradas correctas
writer.write(key, 'Mi primer mensaje')
writer.write(key, 'Mi segundo mensaje')

# Escritura de una entrada corrupta, retomando la función de escritura, calculando mal la huella
pickled = pickle.dumps('Mi tercer mensaje')
digest = SimulatedWriter.make_digest(key, b'Huella de alguna cosa diferente al mensaje')
#print(digest)
simulated.write(digest + b' ' + bytes(str(len(pickled)), 'utf-8') + b'\n' + pickled)
simulated.flush()

# Lecturas
print('Lectura del primer mensaje con la clave correcta')
print(reader.read(key))
print('Lectura del segundo mensaje con una clave incorrecta')
print(reader.read(b'sin la clave correcta'))
print('Lectura del tercer mensaje (corrupto) con una clave correcta')
print(reader.read(key))

