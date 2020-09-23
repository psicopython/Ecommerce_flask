from .register import register
from .login    import login

from flask import (
	Blueprint, jsonify,
)

def index():
	return jsonify({
		"API": {
			"version": "v1", "author": "Etho"
		}
	}),200

bp = Blueprint(
	"resource",
	__name__.split(".")[0],
	url_prefix="/api/v1",
)

bp.add_url_rule(
	"/",
	methods=["GET"],
	view_func=index,
	endpoint="index",
)

bp.add_url_rule(
	"/cadastro/",
	methods=["POST"],
	view_func=register,
	endpoint="register",
)

bp.add_url_rule(
	"/login/",
	methods=["POST"],
	view_func=login,
	endpoint="login",
)
