from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# --- Creating SQLAlchemy DB Connection
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
db_s = SQLAlchemy(app)

# --- Creating MovieModel class used with SQLAlchemy DB
class MovieModel(db_s.Model):
	id = db_s.Column(db_s.Integer, primary_key=True)
	name = db_s.Column(db_s.String, nullable=False)
	video_type = db_s.Column(db_s.String, nullable=False)

# --- Creating SQLAlchemy DB 
#db_s.create_all()
#db_s.session.add(MovieModel(id=13860428, name='The Big Lebowski', video_type='Blu-Ray'))
#db_s.session.add(MovieModel(id=54456119, name="The Shawshank Redemption", video_type="DVD"))
#db_s.session.add(MovieModel(id=13264003, name="Casablanca", video_type="DVD"))
#db_s.session.add(MovieModel(id=12954218, name="Gone with the Wind", video_type="DVD"))
#db_s.session.add(MovieModel(id=35645454, name="Pacific Rim", video_type="Blu-Ray"))
#db_s.session.commit()