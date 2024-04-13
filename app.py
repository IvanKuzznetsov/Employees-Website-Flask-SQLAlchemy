import os

from flask import Flask, render_template

from database import db, Employee

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


with app.app_context():
    db.create_all()


@app.route("/")
def all_employees():
    employees = Employee.query.all()
    return render_template("all_employees.html", employees=employees)


if __name__ == '__main__':
    app.run()
