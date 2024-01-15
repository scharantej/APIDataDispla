 ## Flask Application Design

### HTML Files

**1. index.html**
- This is the main HTML file that will serve as the user interface.
- It should contain the following elements:
  - A form with a single input field labeled "MRN" for the user to enter the medical record number.
  - A submit button to trigger the API call and display the results.
  - A section to display the results of the API call, with 10 fields for each piece of data returned by the API.

**2. results.html**
- This HTML file will be used to display the results of the API call.
- It should contain the following elements:
  - A table with 10 columns, each representing a field of data returned by the API.
  - The data from the API call should be populated into the table cells.

### Routes

**1. @app.route('/')**
- This route will handle the main page of the application, which is the index.html file.
- It should render the index.html file when the user accesses the root URL of the application.

**2. @app.route('/results', methods=['POST'])**
- This route will handle the API call and display the results.
- It should:
  - Retrieve the MRN entered by the user from the request form.
  - Make an API call to the specified endpoint with the MRN as a parameter.
  - Parse the response from the API call and extract the relevant data.
  - Render the results.html file, passing the extracted data as a variable.