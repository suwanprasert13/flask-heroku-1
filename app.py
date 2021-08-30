from flask import Flask, jsonify
from flask import Flask, render_template, Response
import cv2


data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
    return "Hello Flask-Heroku"

@app.route('/test')
def tes():
        return "สวัสดี"

if __name__ == "__main__":
    app.run(debug=True)
