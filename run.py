# project/run.py

import os
from project import app

# Heroku = True -> ejecuta para Heroku,
# Heroku = False -> para ejecutar en local
# heroku create -> SOLO primera vez para crear la app (depues de hacer el Procfile y logear con heroku login)
# git push heroku master -> Para suburlo a Heroku
# heroku ps -> vemos si esta correindo
# heroku open -> abrimos la app
# heroku logs  -> vemos los logs en heroku
HEROKU = True

if __name__ == '__main__':
    # El puerto lo da Heroku y es aleatorio, lo debo de coger en tiempo real del entorno.
    # si no existe la variable PORT, uará el valor 5000
    port = int(os.environ.get('PORT', 5000))
    if HEROKU:
        app.run(host='0.0.0.0', port=port)
    else:
        app.run()
