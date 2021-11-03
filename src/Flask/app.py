from flask import Flask

app = Flask(__name__)

@app.route("/users/<name>")
def user(name):
    return "<h1>Hello {}!</h1>".format(name)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

if __name__ == "__main__":
    app.run(debug=True)