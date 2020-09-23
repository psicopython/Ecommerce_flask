
def configGeral(app):
	
	app.config["SECRET_KEY"] = "XaTuBa1234@ç"
	app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://flask:flask@localhost/ecommerce"
	#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False