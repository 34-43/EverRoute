from flask import Flask, render_template, request
import config
import datetime as dt
from datahandler import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    # result = None
    # if request.method == 'POST':
    #     result = request.form.get('my_checkbox')
    dh = datahandler()
    dh.update()
    dh.use_route(1)

    return render_template('index.html',MAPS_KEY=config.maps_key)

if __name__ == '__main__':
    app.run(debug=True)