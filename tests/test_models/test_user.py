#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from models.user import User
from models import storage

# Create a new user
user = User(email="user@example.com", password="mypassword")
storage.new(user)
storage.save()

# Check the password
print("Initial hashed password:", user.password)  # This should print the hashed password

# Update the user's password
user.password = "newpassword"
storage.save()

# Check the updated password
print("Updated hashed password:", user.password)  # This should print the hashed new password
