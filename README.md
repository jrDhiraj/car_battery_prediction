# 🔋 Electronic Car Battery Life Prediction

This project predicts the **health and remaining life of an electronic car battery** using **Deep Learning (ANN)**. Built with **Python, Flask, and Scikit-learn**, the app provides a user-friendly web interface for real-time predictions based on input parameters.

---

## 🚀 Features

* Predicts **car battery health and life expectancy** using Artificial Neural Networks (ANN).
* Clean **Flask web interface** for interactive use.
* Trained on a **Kaggle dataset** for accuracy and reliability.
* Modular, easy-to-understand **Python code structure**.
* Ready to deploy locally or on cloud platforms.

---

## 🧠 Tech Stack

| Category         | Tools / Libraries                    |
| ---------------- | ------------------------------------ |
| Language         | Python                               |
| Framework        | Flask                                |
| Machine Learning | Scikit-learn, TensorFlow/Keras (ANN) |
| Data Handling    | Pandas, NumPy                        |
| Frontend         | HTML, CSS, Jinja2 Templates          |

---

## 📂 Project Structure

```
car_battery_prediction/
│
├── app.py                # Main Flask application
├── model.pkl             # Trained ANN model
├── static/               # CSS and image files
├── templates/            # HTML templates
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
└── .gitignore            # Ignored files (e.g., .venv)
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/jrDhiraj/car_battery_prediction.git
cd car_battery_prediction
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate       # For Windows
# source .venv/bin/activate  # For Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

```bash
python app.py
```

Then open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 📊 Dataset

* **Source:** [Kaggle Dataset on Car Battery Life Prediction](https://www.kaggle.com/)
* Used for training and validating the ANN model.

---

## 🔍 Example Prediction

The model takes user inputs like voltage, temperature, current, and usage duration to predict:

> **Battery Condition:** Healthy / Weak / Replace Soon

---

## 🧑‍💻 Author

**Dhiraj Kumar Sharma**
Engineering Student | Data Science & AI Enthusiast

🌐 [GitHub](https://github.com/jrDhiraj)
💼 [LinkedIn](https://www.linkedin.com/in/dhiraj-kumar-sharma-9054a5243/)

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 💡 Future Improvements

* Integrate real-time IoT battery sensor data.
* Deploy on Render / AWS / Azure.
* Add mobile-friendly UI for live monitoring.
