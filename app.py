import os

from flask import Flask, render_template

from database import db, Employee, Department

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


with app.app_context():
    db.drop_all()
    db.create_all()

    development = Department(name="Разработка")
    db.session.add(development)

    hr = Department(name="Рекрутинг")
    db.session.add(hr)

    db.session.add(
        Employee(
            fullname="Мария Петрова",
            department=development,
        )
    )
    db.session.add(
        Employee(
            fullname="Петя Иванов",
            department=development,
        )
    )
    db.session.add(
        Employee(
            fullname="Тамара Сидорова",
            department=hr,
        )
    )

    db.session.commit()


@app.route("/")
def all_employees():
    employees = Employee.query.all()
    return render_template("all_employees.html", employees=employees)


@app.route("/department/<int:department_id>")
def employees_by_department(department_id):
    department = Department.query.get_or_404(department_id)
    return render_template(
        "employees_by_department.html",
        department_name=department.name,
        employees=department.employees
    )


if __name__ == '__main__':
    app.run()
