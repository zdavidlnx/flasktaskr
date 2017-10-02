# project/run.py

import os
from project import app

# Heroku true -> ejecuta para Heroku, con False, para ejecutar en local
HEROKU = True

if __name__ == '__main__':
    # El puerto lo da Heroku y es aleatorio, lo debo de coger en tiempo real del entorno.
    # si no existe la variable PORT, uará el valor 5000
    port = int(os.environ.get('PORT', 5000))
    if HEROKU:
        app.run(host='0.0.0.0', port=port)
    else:
        app.run()


