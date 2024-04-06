from flask import Flask

app = Flask("ceva aplicatie")

@app.route("/")
def home():
    return "<p>alex plm</p>"

if __name__ == '__main__':
    app.run(debug=True)
    
