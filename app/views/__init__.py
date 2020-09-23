from . import webui
from . import resource

def configViews(app):
	app.register_blueprint(webui.bp)
	app.register_blueprint(resource.bp)