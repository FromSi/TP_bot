import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ujwkfqgxivnzcm:8a175afe5eec296c384ded6610c5da009833e5bc54521e8a9830855238169da1@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/d6kk63qd4nj37e'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


from bot import routes