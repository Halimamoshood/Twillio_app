from flask import Flask
from waitress import serve

from sms_app.services import home, send_sms

app = Flask(__name__)
# sess = session()
app.secret_key = 'super secret key'

@app.route('/')
def home_api():
    return home()

@app.route('/send')
def send_sms_api():
    return send_sms()


if __name__ == '__main__':

    serve(app)