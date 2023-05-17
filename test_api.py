# coding=utf-8
"""
@Project: StressTestLocust
@File: /test_api.py
@Author: Dustin Lin
@Created on: 2023/5/17 13:52:43
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main_page():
    return {
        "message": "200 OK",
        "func": "index"
    }


@app.route("/test1")
def test1():
    return {
        "message": "200 OK",
        "func": "test1"
    }


@app.route("/test2")
def test2():
    return {
        "message": "200 OK",
        "func": "test2"
    }


@app.route("/test3")
def test3():
    return {
        "message": "200 OK",
        "func": "test3"
    }


@app.route("/post", methods=["POST"])
def post():
    return {
        "message": "200 OK",
        "func": "post"
    }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7777)
