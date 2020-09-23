from app.model.users import Users

from flask import (
	Blueprint, jsonify, render_template,
)


def index():
	return jsonify(Users.query.all()[0].getJson()), 200

def cadastro():
	return render_template("register.html")
	
def login():
	return render_template("login.html")
	

bp = Blueprint(
	"webui",
	__name__.split(".")[0],
	template_folder="views/webui/front/templates",
	#static_folder="front/static",
)

bp.add_url_rule(
	"/",
	methods=["GET"],
	view_func=index,
	endpoint="index",
)

bp.add_url_rule(
	"/cadastro/",
	methods=["GET"],
	view_func=cadastro,
	endpoint="cadastro",
)

bp.add_url_rule(
	"/login/",
	methods=["GET"],
	view_func=login,
	endpoint="login",
)
