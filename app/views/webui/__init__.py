from flask import (
	Blueprint, jsonify,
)

def index():
	return jsonify({
		"WEB USER INTERFACE": {
			"version": "v1", "author": "Etho"
		}
	}),200

bp = Blueprint(
	"webui",
	__name__.split(".")[0],
	template_folder="./front/templates",
	static_folder="./front/static",
)

bp.add_url_rule(
	"/",
	methods=["GET"],
	view_func=index,
	endpoint="index",
)
