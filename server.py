from flask import Flask, render_template, request
import os

app = Flask(__name__)

YMONEY_APP_ID = os.getenv('YMONEY_APP_ID', '')
YMONEY_PERMISSIONS = os.getenv('YMONEY_PERMISSIONS', 'account-info operation-history')

@app.route("/")
def start():
    return render_template('request_tmp_token.html', YMONEY_APP_ID=YMONEY_APP_ID, YMONEY_PERMISSIONS=YMONEY_PERMISSIONS)

@app.route("/create_token/")
def create_token():
    print(request.args)
    tmp_token = request.args.get('code', '')
    print('tmp_token', tmp_token)
    return render_template('request_peristent_token.html', YMONEY_APP_ID=YMONEY_APP_ID, tmp_token=tmp_token)
