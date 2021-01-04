from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Column


db = SQLAlchemy()


# Simple User dB model
class User(db.Model):
    __tablename__ = 'Users' #tablename

    id = db.Column(db.Integer, primary_key=True) # User iD
    email = db.Column(db.String(), unique=True, nullable=False) # User Email
    username = db.Column(db.String(),unique=True, nullable=False) # User Name
    password = db.Column(db.String(), nullable=False)  # User Password

    """
    Add Method:
    Using: 
      data = User(email = email ....)
      data.insert()
    """
    def insert(self): 
        db.session.add(self)
        db.session.commit()

    """
    Delete Method:
    Using: 
      data = User.query.filter_by(email = email).first()
      data.delete()
    """
    def delete(self):
        db.session.delete(self)
        db.session.commit()   

    """
    Delete Method:
    Using: 
      data.update()
    """
    def update(self):
        db.session.commit()     


    def __repr__(self):
        return f"User('{self.email}')"
