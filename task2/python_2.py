from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:qwerty@localhost:5432/py_sweater'
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "{}".format(self.name)


db.create_all()


@app.route('/', methods=['GET'])
def main():
    return render_template('main.html', messages=Message.query.all())


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['name']

    user = bool(db.session.query(Message).filter_by(name=text).first())
    if not user:
        db.session.add(Message(text))
        db.session.commit()
        v = 'Привіт, {}'.format(text)
        return render_template('main.html', variable=v)
    else:
        v = 'Вже бачилися, {}'.format(text)
        return render_template('main.html', variable=v)


@app.route('/print_list', methods=['GET'])
def print_list():
    line = ''
    for msg in db.session.query(Message).order_by(Message.name.asc()).all():
        line = line + str(msg) + "<br>"
    html = """<html>
    <head></head>
    <body style="background-color: aliceblue; font-size: 20px; text-align:center">    
    <p>Список тих, з ким вже привіталися: </p>
    """ + line + """
    </body>
    </html>
    """
    return html


if __name__ == '__main__':
    app.run(debug=True)
