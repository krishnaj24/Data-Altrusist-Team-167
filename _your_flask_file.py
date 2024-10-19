from flask import Flask, render_template, request
import joblib  # if you used joblib to save the model

# Initialize Flask
app = Flask(__name__)

# Load your trained model
model = joblib.load('fake_news_model.pkl')  # Replace with your model's path
vectorizer = joblib.load('vectorizer.pkl')  # Replace with your vectorizer's path

# Define the home route to serve the HTML page
@app.route('/')
def index():
    return render_template('front.html')  # Ensure your front.html is in the templates folder

# Route to process form data and give prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    input_text = request.form['input_text']
    
    # Process the input
    processed_text = vectorizer.transform([input_text])  # Transform the input using your vectorizer

    # Use the model to make a prediction
    prediction = model.predict(processed_text)  # Make sure this matches your model input

    # Return the result back to the HTML page
    return render_template('front.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, port=5002)  # You can change the port if necessary
