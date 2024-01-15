 
# Import necessary libraries
from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    """
    Render the main page with the input form.
    """
    return render_template('index.html')

# Define the route to handle the API call and display results
@app.route('/results', methods=['POST'])
def results():
    """
    Handle the API call, parse the response, and render the results page.
    """
    # Retrieve the MRN from the request form
    mrn = request.form.get('mrn')

    # Make the API call with the MRN as a parameter
    # Replace 'API_ENDPOINT' with the actual API endpoint
    response = requests.get(f'API_ENDPOINT?mrn={mrn}')

    # Parse the response from the API call
    data = response.json()

    # Extract the relevant data from the API response
    # Replace 'FIELD_NAMES' with the actual field names returned by the API
    field_names = ['FIELD_NAMES']
    data_list = [data[field] for field in field_names]

    # Render the results page, passing the extracted data
    return render_template('results.html', data=data_list)

# Run the app
if __name__ == '__main__':
    app.run()
