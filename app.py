from flask import Flask
from flask import render_template

app = Flask("ceva aplicatie")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def loging():
    return render_template("login.html")

@app.route("/signup")
def signing():
    return render_template("sign_up.html")

if __name__ == '__main__':
    app.run(debug=True)
    
