from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "WELCOME TO MY WEBSITE"
@app.route("/contact")
def ContactPage():
    return "CONTACT PAGE"
@app.route("/home")
def Homepage():
    return "WELCOME TO HOME PAGE"
@app.route("/gallery")
def Gallery():
    return "Add your photos "


if __name__ == "__main__":
    app.run()