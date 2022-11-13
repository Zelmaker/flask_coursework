from app import app, db
from flask import render_template, request, redirect
from models import Employees


@app.route('/')
def index():
    employees = db.session.query(Employees).all()
    return render_template('index.html', employees=employees)


@app.route('/insert', methods = ['GET', 'POST'])
def insert():
    if request.method == "POST":
        res = request.form.to_dict()
        employee = Employees(
            name = res['name'],
            email = res['email'],
            phone = res['phone']
        )
        db.session.add(employee)
        db.session.commit()
        return redirect('/')


@app.route('/update/', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        data = request.form.to_dict()
        row = db.session.query(Employees).get(data['id'])
        row.name = data['name']
        row.email = data['email']
        row.phone = data['phone']

        db.session.add(row)
        db.session.commit()
        return redirect('/')


@app.route('/delete/<int:id>')
def delete(id: int):
    employee = db.session.query(Employees).get(id)

    db.session.delete(employee)
    db.session.commit()
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)