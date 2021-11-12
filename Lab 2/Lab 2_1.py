import requests
import folium
from flask import Flask, render_template

m = folium.Map(location=[45.5236, -122.6750])

m.save("home.html")

app = Flask(__name__)
@app.route('/')
def render_map():
    return render_template('home.html')

render_map
app.run(debug=True)