import sys, json, requests
from flask import Flask, request
import pyowm
import apiai

app = Flask("MyApp_2")

@app.route('/', methods=['GET', 'POST'])
def receive_message():
    return "Hello World!"


app.run(debug=True)
