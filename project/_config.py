import os

# obtenemos la carpeta donde está este script
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True

"""
    Se ha generado usando:
    
    import os
    os.urandom(24)
"""
SECRET_KEY = b'\xb03V\xf7\x81\xeb\xfd\x1f\xda\x97m\x9faO~\xf7\x1a\x03UT\x82r\x0f\xae'

# Definimos el path completo a la base de datos
DATABASE_PATH = os.path.join(basedir, DATABASE)
