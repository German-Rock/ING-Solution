# Import User model
from . import db
from models import User

# Create a new user with user_type set to "admin"
admin_user = User(
    email='admin@gmail.com',
    password='adminadmin',  # Remember to hash the password before storing it
    first_name='Admin',
    user_type='admin',  # Set user_type to "admin"
    localitate='AdminLocalitate',
    strada='AdminStrada',
    bloc='AdminBloc'
)

# Add the user to the database session
db.session.add(admin_user)

# Commit the changes to persist the user in the database
db.session.commit()