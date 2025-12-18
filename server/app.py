from flask import Flask, make_response, request
from flask_migrate import Migrate
from models import db, Speciality

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

migrate = Migrate(app, db)


@app.route('/')
def home():
    return "Welcome to our Clinic"

@app.route('/specialities', methods=['POST'])
def speciality():
    speciality_name = request.form.get('name')

    new_speciality = Speciality(name=speciality_name)

    db.session.add(new_speciality)
    db.session.commit()

    return make_response(new_speciality, 200)



if __name__ == '__main__':
    app.run(port=5555, debug=True)

