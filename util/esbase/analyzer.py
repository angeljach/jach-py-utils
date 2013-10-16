#!/usr/bin/python

import os
import re

class Analyzer:
	"""ESSMSH Analyzer
		The principal goal of this application is to kill active sessions, using _displaySessions.msh
		to validate the active sessions, and _unloadapp.msh to kill them.

		Authors:
			Angel Cruz Hernandez
			Santiago Vazquez Diaz
	"""
	def __init__(self, folder_path_out, user, password):
		print ('Iniciando Analyzer')
		self.folder_path_out = folder_path_out
		self.user = user
		self.password = password

	def extract_applications(self, file_name):
		req_lines = []
		f = open(file_name, 'r')
		for line in f:
			### Usar 381 en WINDOWS
			if (len(line) == 382):
				application = line[1:20].strip()
				app_status = line[281:300].strip()
				if (app_status == '2'):
					req_lines.append(application)
		f.close()
		return req_lines
	
	def display_sessions(self, cubes_list):
		for cube in cubes_list:
			line_to_execute = "essmsh _displaySessions.msh %s %s Eismp1 %s 1> %s 2>> %s" % (self.user, self.password, cube, self.folder_path_out + cube + '.txt', self.folder_path_out + 'sessi.err')
			print('Ejecutando: ' + line_to_execute)
			### Descomentar la siguiente linea cuando se quiera ejecutar el comando
			#os.system(line_to_execute)

	def kill_active_sessions(self, cubes_list):
		for cube in cubes_list:
			file_name = self.folder_path_out + cube + '.txt'
			print('Analizando: ' + file_name)
			f = open(file_name, 'r')
			for line in f:
				p = re.search( r'.\[(\w+)\].', line, re.M|re.I)
				if p:
					if (int(p.group(1)) == 0):
						print ('Baja de la aplicacion sin sessiones')
						line_to_execute = "essmsh _unloadapp.msh %s %s Eismp1 %s 1> %s 2>> %s" % (self.user, self.password, cube, self.folder_path_out + 'unload.txt', self.folder_path_out + 'unload.err')
						print('Ejecutando: ' + line_to_execute)
						### Descomentar la siguiente linea cuando se quiera ejecutar el comando
						#os.system(line_to_execute)
					else:
						#TODO Definir la funcionalidad
						print('Sesiones activas no encontradas para el cubo ' + cube)