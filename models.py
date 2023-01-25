from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# address Class/Model
class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100))
    city = db.Column(db.String(100))
    street = db.Column(db.String(100)) # street name only
    postal = db.Column(db.String(100)) # postal code

    def __init__(self, country, city, street, postal):
        self.country = country
        self.city = city
        self.street = street
        self.postal = postal

class AddressSchema(ma.Schema):
    class Meta:
        fields = ('id', 'country', 'city', 'street', 'postal')


# user Class/Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100)) 
    last_name = db.Column(db.String(100)) 

    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password', 'first_name', 'last_name') 



# initialize adress schema
address_schema = AddressSchema()
addresses_schema = AddressSchema(many=True)


