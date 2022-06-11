#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Ilustración del funcionamiento de un parser de argumentos
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


import argparse


datas = {
	'cuadrados': {'%s' % x:(x+1)**2 for x in range(20)},
	'cubo': {'%s' % x:(x+1)**3 for x in range(20)},
}

def test(namespace):
	return namespace

def available_keys(namespace):
	return list(datas.keys())

def get(namespace):
	return '%s:%s' % (
		datas['cuadrados'].get(namespace.value),
		datas['cubo'].get(namespace.value))

def getParser():
	parser = argparse.ArgumentParser(
		prog='./testeur.py',
		description='''Probador para argumentos''',
		epilog='''Ejemplo del capítulo 14'''
	)

	subparsers = parser.add_subparsers(help='commands')

	test_parser = subparsers.add_parser(
		'test',
		description='Test del parser',
		help='Permite probar el parser',
	)
	test_parser.set_defaults(func=test)

	list_parser = subparsers.add_parser(
		'list',
		aliases=['l'],
		description='lista de los datos disponibles',
		help='Permite recuperar la lista de las funcionalidades disponibles',
	)
	list_parser.set_defaults(func=available_keys)

	get_parser = subparsers.add_parser(
		'get',
		description='un valor',
		help='Permite dar todos los valores relativos al argumento'
	)
	get_parser.add_argument(
		'value',
		help='valor'
	)
	get_parser.set_defaults(func=get)

	return parser

if __name__ == "__main__":
	parser = getParser()
	args=parser.parse_args()
	print(args.func(args))


