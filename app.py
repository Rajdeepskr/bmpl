from flask import Flask, render_template, request, redirect
from flask.globals import request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bmpl.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Bmpl(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(200), nullable=False)
    whatsapp = db.Column(db.Integer, nullable=False)
    p1_id = db.Column(db.Integer, nullable=False)
    p2_id = db.Column(db.Integer, nullable=False)
    p3_id = db.Column(db.Integer, nullable=False)
    p4_id = db.Column(db.Integer, nullable=False)
    p5_id = db.Column(db.Integer, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.team_name}"


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        team_name = request.form['team_name']
        whatsapp = request.form['whatsapp']
        p1_id = request.form['p1_id']
        p2_id = request.form['p2_id']
        p3_id = request.form['p3_id']
        p4_id = request.form['p4_id']
        p5_id = request.form['p5_id']
        bmpl = Bmpl(team_name=team_name, whatsapp=whatsapp, p1_id=p1_id,
                    p2_id=p2_id, p3_id=p3_id, p4_id=p4_id, p5_id=p5_id)
        db.session.add(bmpl)
        db.session.commit()

    allBmpl = Bmpl.query.all()
    return render_template('index.html', allBmpl=allBmpl)


# @app.route('/update/<int:sno>', methods=['GET', 'POST'])
# def update(sno):
#     if request.method == 'POST':
#         title = request.form['title']
#         desc = request.form['desc']
#         todo = Todo.query.filter_by(sno=sno).first()
#         todo.title = title
#         todo.desc = desc
#         db.session.add(todo)
#         db.session.commit()
#         return redirect('/')

#     todo = Todo.query.filter_by(sno=sno).first()
#     return render_template('update.html', todo=todo)


# @app.route('/delete/<int:sno>')
# def delete(sno):
#     todo = Todo.query.filter_by(sno=sno).first()
#     db.session.delete(todo)
#     db.session.commit()
#     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
