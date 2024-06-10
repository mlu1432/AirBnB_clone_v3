# AirBnB Clone - RESTful API

This project is a RESTful API for the AirBnB clone, built with Flask and SQLAlchemy.

## Project Structure

├── api
│   ├── __init__.py
│   └── v1
│       ├── __init__.py
│       ├── app.py
│       └── views
│           ├── __init__.py
│           ├── amenities.py
│           ├── cities.py
│           ├── index.py
│           ├── places.py
│           ├── places_reviews.py
│           ├── states.py
│           └── users.py
└── models
    ├── amenity.py
    ├── base_model.py
    ├── city.py
    ├── place.py
    ├── review.py
    ├── state.py
    └── user.py

#Endpoints

Status
GET /api/v1/status
Returns the status of the API.
Stats
GET /api/v1/stats
Retrieves the number of each object by type.
States
GET /api/v1/states

Retrieves the list of all State objects.
GET /api/v1/states/<state_id>

Retrieves a State object.
DELETE /api/v1/states/<state_id>

Deletes a State object.
POST /api/v1/states

Creates a State.
PUT /api/v1/states/<state_id>

Updates a State object.
Cities
GET /api/v1/cities

Retrieves the list of all City objects.
GET /api/v1/cities/<city_id>

Retrieves a City object.
DELETE /api/v1/cities/<city_id>

Deletes a City object.
POST /api/v1/cities

Creates a City.
PUT /api/v1/cities/<city_id>

Updates a City object.
Amenities
GET /api/v1/amenities

Retrieves the list of all Amenity objects.
GET /api/v1/amenities/<amenity_id>

Retrieves an Amenity object.
DELETE /api/v1/amenities/<amenity_id>

Deletes an Amenity object.
POST /api/v1/amenities

Creates an Amenity.
PUT /api/v1/amenities/<amenity_id>

Updates an Amenity object.
Places
GET /api/v1/places

Retrieves the list of all Place objects.
GET /api/v1/places/<place_id>

Retrieves a Place object.
DELETE /api/v1/places/<place_id>

Deletes a Place object.
POST /api/v1/places

Creates a Place.
PUT /api/v1/places/<place_id>

Updates a Place object.
Reviews
GET /api/v1/reviews

Retrieves the list of all Review objects.
GET /api/v1/reviews/<review_id>

Retrieves a Review object.
DELETE /api/v1/reviews/<review_id>

Deletes a Review object.
POST /api/v1/reviews

Creates a Review.
PUT /api/v1/reviews/<review_id>

Updates a Review object.
Users
GET /api/v1/users

Retrieves the list of all User objects.
GET /api/v1/users/<user_id>

Retrieves a User object.
DELETE /api/v1/users/<user_id>

Deletes a User object.
POST /api/v1/users

Creates a User.
PUT /api/v1/users/<user_id>

##Updates a User object.

#Contributing

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make changes.
Commit changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.

#Authors

Aniekeme Francis aniekemeusanga@gmail.com
Lucas Sekwati Luxturesekwati@gmail.com
