from flask_sqlalchemy	import SQLAlchemy
from flask_migrate		import Migrate


db = SQLAlchemy()
mi = Migrate()


def configModel(app):
	"""
	def que configura o db e o migrate
	"""
	db.init_app(app)
	mi.init_app(app,db)
	app.db = db

"""
##########################################

### AS TABELAS VIRAM DEPOIS DISSO AQUI ###

##########################################
"""

from .users import Users