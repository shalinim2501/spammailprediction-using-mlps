from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load model
with open("spam_classifier.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    email = request.form['email']
    prediction = model.predict([email])[0]
    label = "Spam" if prediction == 1 else "Ham"
    return render_template("index.html", prediction_text=f"Prediction: {label}")

if __name__ == '__main__':
    app.run(debug=True)
