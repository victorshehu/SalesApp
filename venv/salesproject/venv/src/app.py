from flask import Flask

app = Flask (__name__) #special variable that let flask know this file

@app.route('/')
def home():
    return "Hello, World!"

app.run(port = 5000)
