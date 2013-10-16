#!/usr/bin/python
from analyzer import Analyzer

file_path_app = '/home/jach/Downloads/apps.txt'
folder_path_out = '/home/jach/Downloads/'

#TODO: Esto debe ser obtenido a partir de la linea de comando
user_name = 'admin'
password = 'password123'

a = Analyzer(folder_path_out, user_name, password)

l_app = a.extract_applications(file_path_app)
a.display_sessions(l_app)

### En caso de requerir esperar un tiempo, aqui puedes poner el time.sleep(5)

#a.kill_active_sessions(l_app)