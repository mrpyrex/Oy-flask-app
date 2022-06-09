from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'IamVeryImportant'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

@app.route("/")
def greeting():
    return render_template("greeting.html")

@app.route("/about")
def about():
    return render_template("about.html", title="About OY")

if __name__ == '__main__':
    app.run(debug=True)