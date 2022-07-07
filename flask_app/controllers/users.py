from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users = User.get_all()
    return render_template("read.html", users = users)

@app.route('/users/new')
def new():
    return render_template("create.html")

@app.route('/create/user', methods=['POST'])
def create_user():
    User.save(request.form)
    return redirect('/users')


@app.route('/users/<int:id>')
def show_user(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    return render_template("show.html", user=user )

@app.route('/users/<int:id>/edit')
def show_edit(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    return render_template("edit.html", user=user )

@app.route('/users/<int:id>/update', methods = ['POST'])
def update_user(id):
    User.update(request.form)
    return redirect('/users')



@app.route('/users/<int:id>/delete')
def show_deleted(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/users')


