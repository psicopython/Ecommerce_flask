from app.config import configGeral
from app.views  import configViews
from app.model  import configModel


from flask import Flask

def CreateApp():
	"""
	Def principal: cria, configura e retorna um app
	"""
	app = Flask(__name__.split(".")[0])
	
	configGeral(app)
	configModel(app)
	configViews(app)

	return app

