# import Flask, render_template, jsonify
from flask import Flask, render_template, jsonify

# import Pictures
from pictures_data import *

# create Flask app
app = Flask(__name__)


# --- API Routes ---
@app.route('/api/pictures')
def pictures():
    return jsonify(Pictures)

@app.route('/api/pictures/<int:id>')
def picture_id(id):
    for picture in Pictures:
        if picture['id'] == id:
            return jsonify(picture)

@app.route('/api/pictures/<country>')
def pic_country(country):
    for picture in Pictures:
        if picture['country'] == country:
            return jsonify(picture)


# --- HTML Routes ---
@app.route('/html/pictures')
def html_pictures():
    pictures = Pictures
    return render_template('pictures_index.html', pictures = pictures)

@app.route('/html/pictures/<int:id>')
def html_picture_id(id):
    for picture in Pictures:
        if picture['id'] == id:
            return render_template('picture_show.html', picture = picture)
    return "<h1>Sorry, no there is no picture with that id!</h1>"

@app.route('/html/pictures/<country>')
def html_picture_country(country):
    pictures =[]
    for picture in Pictures:
        if picture['country'].lower() == country.lower():
            pictures.append(picture)
            return render_template('pictures_index.html', pictures = pictures)

# run our Flask app
if __name__ == '__main__':
    app.run(debug=True)
