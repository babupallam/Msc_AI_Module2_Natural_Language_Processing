from bottle import route, run, template, request
from predict import *
import torch

# Route to display the form and show the prediction
@route('/')
def index():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Prediction App</title>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                }
                .container {
                    width: 100%;
                    max-width: 600px;
                    margin: 50px auto;
                    background: #fff;
                    padding: 20px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }
                h1 {
                    text-align: center;
                    color: #333;
                }
                form {
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                    margin-top: 20px;
                }
                input[type="text"] {
                    padding: 10px;
                    font-size: 16px;
                    border-radius: 5px;
                    border: 1px solid #ccc;
                }
                input[type="submit"] {
                    padding: 10px;
                    font-size: 16px;
                    background-color: #28a745;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s ease;
                }
                input[type="submit"]:hover {
                    background-color: #218838;
                }
                footer {
                    text-align: center;
                    margin-top: 20px;
                    color: #777;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Language Prediction Based on Name</h1>
                <form action="/predict" method="post">
                    <label for="input_line">Enter a name:</label>
                    <input id="input_line" name="input_line" type="text" required/>
                    <input value="Predict" type="submit" />
                </form>
            </div>
            <footer>
                <p>Powered by Bottle & PyTorch</p>
            </footer>
        </body>
        </html>
    '''

# Route to handle the form submission and return the prediction
@route('/predict', method='POST')
def predict_name():
    input_line = request.forms.get('input_line')  # Get the user input from the form
    result = predict(input_line, 10)  # Call your predict function to get predictions

    # Convert tensor result to a JSON-serializable list (assuming multiple predictions)
    if isinstance(result, torch.Tensor):
        result = result.tolist()  # Convert tensor to list if it is multi-dimensional

    # Check if result is a list, if not, wrap it in a list for consistency
    if not isinstance(result, list):
        result = [result]

    # Render the result in a nicely styled webpage with the winner highlighted
    return template('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Prediction Result</title>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                }
                .container {
                    width: 100%;
                    max-width: 600px;
                    margin: 50px auto;
                    background: #fff;
                    padding: 20px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }
                h1 {
                    text-align: center;
                    color: #333;
                }
                p {
                    font-size: 18px;
                    color: #555;
                }
                ol {
                    padding-left: 20px;
                }
                li {
                    font-size: 18px;
                    color: #555;
                    margin-bottom: 10px;
                }
                .winner {
                    color: #e63946;
                    font-weight: bold;
                }
                a {
                    text-decoration: none;
                    color: #28a745;
                    font-weight: bold;
                    display: inline-block;
                    margin-top: 20px;
                }
                footer {
                    text-align: center;
                    margin-top: 20px;
                    color: #777;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Prediction Result</h1>
                <p><strong>Input:</strong> {{input_line}}</p>
                <p><strong>Predictions:</strong></p>
                <ol>
                    <li class="winner">{{result[0]}}</li> <!-- Highlight the first result as the winner -->
                    % for prediction in result[1:]:
                        <li>{{prediction}}</li>
                    % end
                </ol>
                <a href="/">Go back</a>
            </div>
            <footer>
                <p>Powered by Bottle & PyTorch</p>
            </footer>
        </body>
        </html>
    ''', input_line=input_line, result=result)

# Run the server on localhost:5533
run(host='localhost', port=5533)
