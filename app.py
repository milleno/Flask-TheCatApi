from cat_api import CatApi
from flask import Flask, render_template
import flask_monitoringdashboard as dashboard
import datetime
import logging

api = CatApi()

app = Flask(__name__)
dashboard.bind(app)

@app.route('/')
@app.route('/index')
def index():
    app.logger.debug("main debug")
    app.logger.info("main info")
    app.logger.warning("main warning")
    app.logger.error("main error")
    app.logger.critical("main critical")
    return render_template('index.html')

@app.route('/breeds')
def breeds():
    breeds = api.get_breeds()
    return render_template('breeds.html', breeds=breeds)

@app.route('/hat')
def hat():
    return render_template('hat.html')

@app.route('/sunglasses')
def sunglasses():
    return render_template('sunglasses.html')    

@app.route('/breed/<id>')
def breed(id):
    breed_img = api.get_breed_img(id)
    return render_template('breed.html', breed_img=breed_img)

if __name__ == '__main__':
    logging.basicConfig(filename='templates/log.log',level=logging.DEBUG)
    app.run(host="0.0.0.0", debug=True)
