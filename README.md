# 🔥 Car Battery Temperature Prediction

This project predicts whether a **car battery is safe to charge** or **too hot/cold to charge** based on temperature and other input parameters.
It uses a **Deep Learning (ANN)** model built with **Python, Flask, and Scikit-learn** to provide instant predictions through a clean web interface.

---

## 🚗 Overview

Battery temperature plays a key role in electric vehicle performance and safety.
Charging a battery at unsafe temperatures can reduce its lifespan or even cause damage.
This project aims to **predict the charging suitability** (Cool / Optimal / Hot) of a battery using temperature-related data.

---

## 🧠 Tech Stack

| Category         | Tools / Libraries           |
| ---------------- | --------------------------- |
| Language         | Python                      |
| Framework        | Flask                       |
| Deep Learning    | TensorFlow / Keras (ANN)    |
| Machine Learning | Scikit-learn                |
| Data Handling    | Pandas, NumPy               |
| Frontend         | HTML, CSS, Jinja2 Templates |

---

## 🧩 Features

* Predicts **battery temperature condition** (Cool / Normal / Hot).
* Determines whether the battery is **safe to charge or not**.
* Built with an **Artificial Neural Network (ANN)** for accurate results.
* Clean and simple **Flask web interface** for live predictions.
* Uses **Kaggle dataset** for training and evaluation.

---

## 📂 Project Structure

```
car_battery_temp_prediction/
│
├── app.py                # Flask application
├── model.pkl             # Trained ANN model
├── static/               # CSS and assets
├── templates/            # HTML templates
├── requirements.txt      # Dependencies list
├── README.md             # Project documentation
└── .gitignore            # Ignore files (like .venv)
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/jrDhiraj/car_battery_temp_prediction.git
cd car_battery_temp_prediction
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

### 4. Run the Application

```bash
python app.py
```

Visit in your browser:

```
http://127.0.0.1:5000/
```

---

## 📊 Dataset

* **Source:** [Kaggle – Car Battery Temperature Dataset](https://www.kaggle.com/)
* Features include: ambient temperature, voltage, current, internal resistance, etc.
* The model classifies temperature conditions and charging safety.

---

## 🔍 Example Prediction

Input Example:

| Parameter           | Value  |
| ------------------- | ------ |
| Voltage             | 12.6 V |
| Ambient Temperature | 35°C   |
| Internal Resistance | 0.03 Ω |

Output Example:

> **Prediction:** Hot — *Unsafe to Charge*

---

## 🧑‍💻 Author

**Dhiraj Kumar Sharma**
Engineering Student | Deep Learning & AI Enthusiast

🌐 [GitHub](https://github.com/jrDhiraj)
💼 [LinkedIn](https://www.linkedin.com/in/dhiraj-kumar-sharma-9054a5243/)

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🚀 Future Enhancements

* Integrate with real-time car sensors (IoT).
* Add temperature-based alerts in the web dashboard.
* Deploy on **Render / Railway / AWS EC2** for public access.
