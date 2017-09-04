# project/db_create.py

from views import db
from models import Task
from datetime import date


# Creamos la base de datos y la tabla
db.create_all()


# Insertamos los datos de ejemplo
db.session.add(Task("Finish this tutorial", date(2017, 8, 22), 10, 1))
db.session.add(Task("Finish Real Python", date(2017, 11, 23), 10, 1))
db.session.add(Task("Revisar SQLAlchemy", date(2017, 10, 12), 10, 0))

# Commit de los cambios
db.session.commit()


