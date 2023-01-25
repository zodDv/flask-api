from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash # generate hash
from flask_jwt_extended import create_access_token, jwt_required
from models import Address, User, address_schema, addresses_schema
from config import db, app

# create an adress
@app.route('/address', methods=['POST'])
@jwt_required()
def add_adress():
    country = request.json['country']
    city = request.json['city']
    street = request.json['street']
    postal = request.json['postal']

    new_address = Address (country, city, street, postal)

    db.session.add(new_address)
    db.session.commit()
  
    return address_schema.jsonify(new_address)

# Get all addresses
@app.route('/address', methods=['GET'])
@jwt_required()
def get_addresses():
    all_addresses = Address.query.all()
    result = addresses_schema.dump(all_addresses)
    return jsonify(result)

# Get a single address
@app.route('/address/<id>', methods=['GET'])
@jwt_required()
def get_address(id):
    address = Address.query.get_or_404(id)
    return address_schema.jsonify(address)


# Update a address
@app.route('/address/<id>', methods=['PUT'])
@jwt_required()
def update_address(id):
    address = Address.query.get_or_404(id)
    
    country = request.json['country']
    city = request.json['city']
    street = request.json['street']
    postal = request.json['postal']

    address.country = country
    address.city = city
    address.street = street
    address.postal = postal

    db.session.commit()

    return address_schema.jsonify(address)

# Delete a address
@app.route('/address/<id>', methods=['DELETE'])
@jwt_required()
def delete_address(id):
    address = Address.query.get_or_404(id)
    db.session.delete(address)
    db.session.commit()
    
    return address_schema.jsonify(address)


# create an users
@app.route('/signup', methods=['POST'])
def signup():
    email = request.json['email']
    password = request.json['password']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    user = User.query\
        .filter_by(email = email)\
        .first()
    if not user:
        # database ORM object
        user = User(
        
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = generate_password_hash(password)
        )
        # insert user
        db.session.add(user)
        db.session.commit()
  
        return make_response('Successfully registered.', 201)
    else:
        # returns 202 if user already exists
        return make_response('User already exists. Please Log in.', 202)
    

@app.route("/login", methods=["POST"])
def login():
    email = request.json['email']
    password = request.json['password']

    if not email or not password:
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )
  
    user = User.query\
        .filter_by(email = email)\
        .first()
  
    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )
  
    if check_password_hash(user.password, password):
        # generates the JWT Token
        access_token = create_access_token(identity=user.id)  # default exp is 15 minutes 
  
        return make_response(jsonify({'token' : access_token}), 201)
    # returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
    )


if __name__ == '__main__': 
    with app.app_context(): 
        db.create_all()   
    app.run(debug=True)

