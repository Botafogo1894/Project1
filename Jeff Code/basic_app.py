# import flask here
from flask import Flask, render_template

# create new Flask App here
app = Flask(__name__)

# define routes for your new flask app
@app.route('/')
def index():
    return "<h1>Welcome to my flaks app</h>,<p>be careful, it's still under construction...</p>"

@app.route('/profile/<username>')
def user_profile(username):
    return render_template('basic.html', username = username.title())

@app.route('/profile/<name>/<age>/<favorite_hobby>/<hometown>')
def profile_page(name, age, favorite_hobby, hometown):
    name = name.title()
    age = int(age)
    hobby = favorite_hobby.title()
    if "_" in hometown:
        town = " ".join([word.title() for word in hometown.split("_")])
    else:
        town = hometown.title()
    return render_template('profile.html', name=name, age=age, hobby=hobby, town=town)

@app.route('/hello-world-template')
def hello_world_template():
    return render_template('hello_world.html')

if __name__ == '__main__':
    app.run(debug=True)
