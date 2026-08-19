# 🧠 Student Stress Level Management

A **Machine Learning-based web application** designed to predict and manage student stress levels using academic, lifestyle, and behavioral factors.

The project uses a trained Machine Learning model and a Streamlit interface to provide an interactive stress-level prediction system.

## 🚀 Live Demo

🔗 **Try the application online:**

[Student Stress Level Management](https://studentstresslevelmanagement-fblzgvyghwuxdmviuvpd3h.streamlit.app/)

## 💻 GitHub Repository

🔗 [View Source Code on GitHub](https://github.com/rishabh4630/student_stress_level_management)

---

## 📌 Project Overview

Student stress can be influenced by multiple academic, personal, and lifestyle factors. This project uses **Machine Learning** to analyze these factors and predict a student's stress level.

The trained model is integrated into a **Streamlit web application**, allowing users to enter relevant information and receive a predicted stress level.

## ✨ Features

* Interactive Streamlit web interface
* Student stress-level prediction
* Machine Learning model integration
* Data preprocessing and scaling
* User-friendly input form
* Real-time prediction
* Saved trained model using Pickle
* Saved scaler for preprocessing
* Simple and interactive results

## 🧠 Machine Learning Workflow

```text
Student Information
        ↓
Data Preprocessing
        ↓
Feature Scaling
        ↓
Trained ML Model
        ↓
Stress Level Prediction
        ↓
Result Display
```

## ⚙️ Technologies Used

* **Python**
* **Streamlit**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Joblib/Pickle**
* **Machine Learning**

## 🤖 Machine Learning Model

The project uses a pre-trained model stored in:

```text
student_stress_model.pkl
```

A saved scaler is also included:

```text
scaler.pk1
```

The application loads these trained components to preprocess user inputs and generate predictions.

## 📁 Project Structure

```text
student_stress_level_management/
│
├── app (1).py
├── student_stress_model.pkl
├── scaler.pk1
├── requirements (1).txt
├── LICENSE
└── README.md
```

The repository currently contains these core application and model files.

## 🔄 How It Works

1. User enters the required student information.
2. The application collects the input features.
3. Input data is preprocessed.
4. The saved scaler transforms the input data.
5. The trained Machine Learning model processes the transformed data.
6. The application predicts the student's stress level.
7. The prediction is displayed through the Streamlit interface.

## 🛠️ Installation

### Clone the Repository

```bash
git clone https://github.com/rishabh4630/student_stress_level_management.git
```

### Navigate to the Project

```bash
cd student_stress_level_management
```

### Install Dependencies

```bash
pip install -r "requirements (1).txt"
```

### Run the Application

```bash
streamlit run "app (1).py"
```

The application will open in your default browser.

## 🎯 Project Objective

The main objective of this project is to demonstrate the use of **Machine Learning for student stress-level prediction** through an easy-to-use web application.

It demonstrates practical implementation of:

* Data preprocessing
* Feature scaling
* Machine Learning
* Model serialization
* Model deployment
* Streamlit application development

## 📈 Future Improvements

* Add multiple Machine Learning algorithms and compare performance
* Display prediction probability
* Add visual analytics and charts
* Add personalized stress-management recommendations
* Improve UI/UX
* Add more student-related features
* Deploy the application with continuous integration

## 👨‍💻 Author

**Rishabh Singh Rajput**

GitHub: (https://github.com/rishabh4630)

## 📜 License

This project is licensed under the **MIT License**. The repository's license identifies Rishabh Singh Rajput as the copyright holder.
