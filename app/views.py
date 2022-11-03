from flask import Flask, render_template, url_for, request, redirect, jsonify
from datetime import datetime
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from app import app, bcrypt, db
from database.db_schema import *
import psutil


@app.route('/users/', methods=['GET'])
def users():
    users_list = User.query.all()
    return jsonify(users=users_schema.dump(users_list))


@app.route('/performance/', methods=['GET'])
def performance():
    performance_list = Performance.query.all()
    return jsonify(performances=performances_schema.dump(performance_list))


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        test = User.query.filter_by(username=username).first()
        if test:
            return jsonify(message='That username is taken!'), 409
        else:
            pin = request.form['pin']
            pw_hash = bcrypt.generate_password_hash(pin)
            user = User(username=username, pw_hash=pw_hash)
            db.session.add(user)
            db.session.commit()
            return jsonify(message='User created successfully.'), 201
    elif request.method == 'GET':
        return render_template('register.html')


@app.route('/login/', methods=['POST'])
def login():
    if request.is_json:
        username = request.json['username']
        pin = request.json['pin']
    else:
        username = request.form['username']
        pin = request.form['pin']
    test = User.query.filter_by(username=username).first()
    if test:
        test_user = User.query.filter_by(username=username).first()
        if bcrypt.check_password_hash(test_user.pw_hash, pin):
            access_token = create_access_token(identity=username)
            return jsonify(message='Login succeeded', access_token=access_token), 201
        else:
            return jsonify(message='Wrong password'), 401
    else:
        return jsonify(message='There is no account with that username'), 401


@app.route("/", methods=['POST', 'GET'])
def base():
    return render_template('base.html')


@app.route("/time/", methods=['GET'])
@jwt_required()
def get_time():
    return jsonify(message=str(datetime.now()))


@app.route('/params/', methods=['GET'])
def params():
    return jsonify(cpu_usage=psutil.cpu_percent(), cpu_stats=psutil.cpu_stats(), cpu_freq=psutil.cpu_freq(),
                   logged_users=psutil.users()[0], disk_usage=psutil.disk_usage('/'),
                   virtual_memory=psutil.virtual_memory())


@app.route('/params/<int:id>/', methods=['GET'])
def params_id(id):
    parameters = Performance.query.filter_by(id=id).first()
    if parameters:
        return jsonify(performance=performance_schema.dump(parameters))
    else:
        return jsonify(message='There is no parameters with that id'), 404


@app.route('/add_params/', methods=['POST'])
def add_params():
    test = Performance.query.filter_by(id=request.form['date']).first()
    if test:
        return jsonify(message='There is already parameters in db from that date.'), 409
    else:
        parameters = Performance(date=request.form['date'], memory_usage=float(request.form['memory_usage']),
                                 CPU_usage=float(request.form['CPU_usage']),
                                 disk_usage=float(request.form['disk_usage']))
        db.session.add(parameters)
        db.session.commit()
        return jsonify(message='You added new parameters!'), 201


@app.route('/update_params/', methods=['PUT'])
def update_params():
    parameters = Performance.query.filter_by(date=request.form['date']).first()
    if parameters:
        parameters.date = request.form['date']
        parameters.memory_usage = float(request.form['memory_usage'])
        parameters.CPU_usage = float(request.form['CPU_usage'])
        parameters.disk_usage = float(request.form['disk_usage'])
        db.session.commit()
        return jsonify(message='You updated parameters!'), 202
    else:
        return jsonify(message='There is no parameters with that id'), 404


@app.route('/delete_params/<int:id>/', methods=['DELETE'])
def delete_params(id):
    parameters = Performance.query.filter_by(id=id).first()
    if parameters:
        db.session.delete(parameters)
        db.session.commit()
        return jsonify(message='You deleted parameters from ' + parameters.date + ' !'), 202
    else:
        return jsonify(message='There is no parameters with that id'), 404
