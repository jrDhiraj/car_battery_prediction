from flask import Flask, request, render_template, jsonify
import numpy as np
import joblib
import tensorflow as tf
import sklearn


# Initialize Flask app
app = Flask(__name__)

# Load model and preprocessing tools
model = tf.keras.models.load_model(r'model/battery_temp_model.h5')
scaler = joblib.load(r'model\scaler (2).pkl')
encoder = joblib.load(r'model\encoder.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        input_data = [
            float(request.form['Capacity']),
            float(request.form['Rct']),
            float(request.form['Re']),
            encoder.transform([request.form['type']])[0]
        ]

        # Scale input and predict
        scaled_input = scaler.transform([input_data])
        prediction = model.predict(scaled_input)
        output = float(prediction[0][0])

        # Add logic for dynamic message
        if output < 20:
            message = f"{output:.2f}°C → Cool temperature. Safe to charge."
        elif 20 <= output < 35:
            message = f"{output:.2f}°C → Normal range. Battery working fine."
        else:
            message = f"{output:.2f}°C → Hot! Avoid charging now."

        return render_template('index.html', prediction_text=message)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
