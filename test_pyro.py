#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Ejemplo de utilización de PyRO
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


import Pyro4


if __name__ == "__main__":
	class Service:
		def hello(self, name):
			return 'hello %s' % name
	daemon=Pyro4.Daemon()
	uri=daemon.register(Service())
	print("URI: %s" % uri)
	daemon.requestLoop()

