from email.policy import default
from os import abort
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from urllib.parse import quote
from flask import jsonify, make_response
from flask_json import FlaskJSON, JsonError, json_response, as_json
import json
import json_fix

app = Flask(__name__)
#initialize 
FlaskJSON(app)
# db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dero:%s@localhost/my_users'% quote('Dextero@135')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://users.db'
#secret key
app.config['Secret_key'] = "my long secret key veryy"
#initialize db
db = SQLAlchemy(app)
#model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, name=None, email=None, date_added=None):
        self.name = name
        self.email = email
        self.date_added = date_added

    def __repr__(self):
        return f'<User {self.name!r}>'
    # create a string
    # def __repr__(self):
    #     return '<Name %r>' % self.name

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.get('/users')
def get_users():
    users = Users.query.all()
    return users
    # return jsonify(users.to_json() for user in users)

@app.get('/users/<int:user_id>')
def get_user(user_id):
    user = Users.query.get(user_id)
    if user is None:
        abort(404)
    # return jsonify(user.to_json)
    # return json_response(user)
    # response = jsonify(user)
    # return json.dumps(user)
    # print(user)

@app.post('/users')
def post_users():
    user = Users(name='Derrick', email='derrickmbugua50@gmail.com')
    db.session.add(user)
    db.session.commit()
    return "success"

@app.route('/us/<int:id>', methods=['PUT'])
def update_post(id):
    user = Users.query.get(id)
    user.name = "Mwema"
    db.session.commit()
    return "sucess"