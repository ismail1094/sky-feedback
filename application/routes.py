from flask import render_template, Flask, request
from application import app

# Create an empty list to store ratings and engineer names
ratings_list = []


# Define a route for the home page
@app.route('/')
def home():
    # Render the 'home.html' template and provide values for placeholders
    return render_template("home.html", customer_name="Bob", engineer_name="Rob")


# Define a route for form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get the 'rating' and 'engineer_name' values from the submitted form data
    rating = request.form.get('rating')
    engineer_name = request.form.get('engineer_name')

    # Create a dictionary with 'engineer_name' as key and 'rating' as value
    rating_dictionary = {engineer_name: rating}

    # Append the dictionary to the 'ratings_list'
    ratings_list.append(rating_dictionary)

    # Print the updated 'ratings_list'
    print(ratings_list)

    # Return a message indicating the submitted rating and engineer name
    return "Rating {} submitted for {}.".format(rating, engineer_name)
