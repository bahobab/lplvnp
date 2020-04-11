import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# from server import connex_app

base_url = 'http://localhost:5001/api/v1/image_file'

basedir = os.path.abspath(os.path.dirname(__file__))
# Create the Connextion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Config the SQLAlchemy part of the app
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + \
    os.path.join(basedir, 'image.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# create the the SQLAlchemy instnce
db = SQLAlchemy(app)

# Initialize marshmallow
ma = Marshmallow(app)


# *************

# Delete database file if it curently exists
# if os.path.exists('image.db'):
#     os.remove('image.db')

# # Create the database
# db.create_all()

# db.session.commit()

print('config initialized...')
