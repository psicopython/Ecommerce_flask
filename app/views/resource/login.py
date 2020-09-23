from app.model.users import Users
from flask import (
	request, abort, session,
)

def login():
	if request.method == "POST":
		data = request.json["user"]
		if data["user"] and data["passwd"]:
			user = Users.query.filter_by(email=data["user"]).first()
			if user:
				if user.checkPass(data["passwd"]):
					#session["user_data"] = f"{user.id}/{user.email}"
					return "ok", 200
				else:
					return "não autorizado",401
			else:
				return "não autorizado",401
		else:
			return "informações parciais",206
	else:
		abort(404)