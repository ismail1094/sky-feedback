from flask import render_template, Flask, request
from application import app

# Create an empty list to store ratings and engineer names
ratings_list = []


# Define a route for the home page
@app.route('/<engineer_name>/<customer_name>')
def home(engineer_name, customer_name):
    # Render the 'home.html' template and provide values for placeholders
    return render_template("home.html", engineer_name=engineer_name, customer_name=customer_name)


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
    return render_template("success.html", rating=rating, engineer_name=engineer_name)
