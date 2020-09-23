from app.model.users import Users

from flask import (
	current_app as app, abort,
	jsonify, request, session,
)
from datetime import datetime


def register():
	if request.method == "POST":
		data = request.json["user"]
		status206 = []
		for item in [
			"tel", "cep", "cpf", "name",
			"email", "passwd","passwd2",
			"state", "city", "address", 
			"lastname","nascimento"]:
				
			if data[item] == "":
				status206.append(item)
		if status206:
			return jsonify(status206), 206
		data["nascimento"] = datetime.strptime(data["nascimento"],"%d/%m/%Y")
		newUser = Users(data)
		app.db.session.add(newUser)
		app.db.session.commit()
		print(newUser)
		return "ok",201
	else:
		abort(404)