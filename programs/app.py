from flask import Flask, render_template, request
import config

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    # result = None
    # if request.method == 'POST':
    #     checkbox_value = request.form.get('my_checkbox')
    #     result = process_checkbox(checkbox_value)

    return render_template('index.html',MAPS_KEY=config.maps_key)

def process_checkbox(val):
    if val == 'on':
        return "checked"
    else:
        return "unchecked"

if __name__ == '__main__':
    app.run(debug=True)