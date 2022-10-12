from email.policy import default
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from urllib.parse import quote

app = Flask(__name__)
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

# DB_USERNAME=dero
# DB_PASSWORD=Dextero@135