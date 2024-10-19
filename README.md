# Data-Altrusist-Team-167
# MedNewsModel - Fake News Healthcare Detection

**MedNewsModel** is a machine learning-based web application aimed at detecting fake news in the healthcare domain, specifically focusing on topics such as medical News and other medical information. The project involves preprocessing healthcare datasets, building and training machine learning models, and integrating these models with a web interface for real-time predictions.

## Features
- **Combining Data**: Extract and combine multiple healthcare-related JSON files into a single CSV file.
- **Preprocessing**: Clean, preprocess, and convert data into vectors for machine learning models.
- **Machine Learning Models**: Trains multiple models such as Logistic Regression, Random Forest, Decision Tree, and Gradient Boosting Classifier to predict fake news.
- **Web Interface**: A simple web interface that allows users to input healthcare news articles and check whether they are fake or real.
- **Flask Integration**: Flask is used to integrate the machine learning model with the HTML interface for real-time predictions.

## Table of Contents
- [Project Flow](#project-flow)
- [Installation](#installation)
- [Usage](#usage)
- [Model Information](#model-information)
- [Contributing](#contributing)
- [License](#license)

## Project Flow

1. **Start**:
   - The process begins with understanding the healthcare datasets in JSON format.

2. **Combining Data**:
   - Data from multiple JSON files is combined into one single DataFrame and saved as a CSV file.

3. **Preprocessing**:
   - Extract relevant data from each JSON file.
   - Preprocess the extracted data, removing unnecessary information and cleaning the text.

4. **Vectorization**:
   - Convert the cleaned data into numerical vectors using techniques like TF-IDF (Term Frequency-Inverse Document Frequency) to make it suitable for machine learning algorithms.

5. **Model Training**:
   - The data is split into training and testing datasets.
   - Multiple machine learning models are trained, including:
     - Logistic Regression
     - Random Forest Classifier
     - Decision Tree
     - Gradient Boosting Classifier

6. **Model Testing**:
   - The trained model is tested with real and fake healthcare news data to evaluate its accuracy.

7. **Web Interface**:
   - A website was created using HTML to allow users to input news articles.
   - Flask was used to connect the machine learning model with the HTML interface for real-time predictions.

8. **End**:
   - The system predicts whether the news is real or fake based on the input.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/MedNewsModel.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd MedNewsModel
   ```

3. **Install the required dependencies:**
   Make sure you have Python installed. Run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**
   ```bash
   python your_flask_file.py
   ```
   The app will start on `http://127.0.0.1:5002/`.

## Usage

1. Open your browser and go to `http://127.0.0.1:5002/`.
2. Enter the healthcare-related news or text in the input box.
3. Click "Check News" to determine whether the input is real or fake news.

## Model Information

The project uses a variety of machine learning models to predict fake news in the healthcare domain. The models include:
- **Logistic Regression**
- **Random Forest Classifier**
- **Decision Tree**
- **Gradient Boosting Classifier**

The data is preprocessed and vectorized before being fed into these models for training and predictions.

### Dataset:
- **FakeHealth Dataset**: JSON files containing healthcare-related news articles, which are processed and converted into a CSV for training.

## Contributing

We welcome contributions! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add a new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.
