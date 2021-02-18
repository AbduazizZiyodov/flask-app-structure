from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

from src import app
from src.settings import db
from src.database.models import User


@app.route('/home')
def HomePage():
    return render_template('pages/home.html')

@app.route('/')
def ServerWorking():
    return jsonify({
        "message": "Server is working",
        "success": True
    })

@app.route('/users', methods = ['GET'])
def UsersGet():
    user_data = User.query.all()
    if not user_data:
        return jsonify({"message": "Data Not Found", "success": False})
    data = []
    for i in user_data:
        result = {
            "username": i.username,
            "email": i.email,
            "password": i.password
        }

        data.append(result)

    return jsonify({"data": data})  