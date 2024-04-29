from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
 
class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String(25), nullable=False)
    skin_color = db.Column(db.String(25), nullable=False)
    favorite =db.relationship("Favorite",backref="person")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    population = db.Column(db.Integer,nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    surface_water_percentage = db.Column(db.String, nullable=False)
    radius = db.Column(db.Float, nullable=False)
    gravity = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "Population": self.Population,
            "Climate": self.Climate,
            "Surface_Water_Percentage": self.Surface_Water_Percentage,
            "Radius": self.Radius,
            "Gravity": self.Gravity
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    # def __repr__(self):
    #     return '<Person %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }