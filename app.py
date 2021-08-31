#from flask import Flask, jsonify
from flask import Flask, render_template, Response, jsonify
import cv2

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Flask-Heroku"

@app.route('/test')
def test():
    return "สวัสดี"

if __name__ == "__main__":
    app.run(debug=True)
