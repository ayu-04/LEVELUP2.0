from flask import Flask
from models import *



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "YOUWANTTOGAYLETSGAY"
db.init_app(app)
app.app_context().push()

with app.app_context():
    db.create_all()
    
from controllers import *

app.run(host='0.0.0.0',port=5000, debug=True)
