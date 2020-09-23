from app.model import db

from datetime import datetime

from werkzeug.security import (
	generate_password_hash,
	check_password_hash,
)

class Users(db.Model):
	
	__tablename__ = "users"
	
	id = db.Column(db.Integer, primary_key=True)
	
	cpf = db.Column(db.String(15), nullable=False, unique=True)
	name = db.Column(db.String(32), nullable=False)
	lastname = db.Column(db.String(32))
	
	tel = db.Column(db.String(14),nullable= True)
	email = db.Column(db.String(64), nullable=False)
	passwd = db.Column(db.String(512), nullable=False)
	
	
	cep = db.Column(db.String(9), nullable=True)
	state = db.Column(db.String(64),nullable=False)
	city = db.Column(db.String(64))
	address = db.Column(db.String(128),nullable=False)
	
	cadastro = db.Column(db.Date, nullable=False)
	nascimento = db.Column(db.Date, nullable=False)
	
	conf_tel = db.Column(db.Boolean, default=False)
	conf_email = db.Column(db.Boolean, default=False)
	
	def __init__(self, data):
			
		self.tel = data["tel"]
		self.cep = data["cep"]
		self.cpf = data["cpf"]
		self.name = data["name"]
		self.email = data["email"]
		self.passwd = self.hashPass(data["passwd"])
		self.state = data["state"]
		self.city = data["city"]
		self.address = data["address"]
		self.lastname = data["lastname"]
		self.nascimento = data["nascimento"]
		self.cadastro = self.getDateNow()
	
	def getDateNow(self):
		return datetime.now()
	
	def hashPass(self, passwd):
		return generate_password_hash(passwd)
		
	def checkPass(self, passwd):
		return check_password_hash(self.passwd, passwd)
	
	def getJson(self):
		return {
			"id": self.id,
			"tel": self.tel,
			"cep": self.cep,
			"cpf": self.cpf,
			"name": self.name,
			"fullname": self.name+" "+self.lastname,
			"lastname": self.lastname,
			"email": self.email,
			"state": self.state,
			"city": self.city,
			"address": self.address,
			"cadastro": self.cadastro.strftime("%d/%m/%Y"),
			"nascimento": self.nascimento.strftime("%d/%m/%Y"),
			"conf_email": self.conf_email,
			"conf_tel": self.conf_tel,
		}
	def __repr__(self):
		return f"< User: {self.id} | {self.name} >"