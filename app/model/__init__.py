from flask_sqlalchemy	import SQLAlchemy
from flask_migrate		import Migrate


db = SQLAlchemy()
mi = Migrate()

"""
###
 OS BANCOS VIRAM DEPOIS DISSO AQUI
###
"""

"""
###
 OS BANCOS VIRAM ANTES DISSO AQUI
###
"""

def configModel(app):
	"""
	def que inicia o db e o migrate
	"""
	db.init_app(app)
	mi.init_app(app,db)
	app.db = db
