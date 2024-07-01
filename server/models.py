from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'

    id = db.Column(db.Integer, primary_key=True)  # Corrected primary_key argument
    magnitude = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(64), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    # The __repr__ method in Python is a special method used to define the "official" string representation of an object. 
    def __repr__(self):
        return f'<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>'
