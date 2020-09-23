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
