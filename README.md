🌍 Human Development Index (HDI) Prediction System

## 📌 Project Overview

The **Human Development Index (HDI) Prediction System** is a Machine Learning-based web application developed as part of the **SmartBridge AI-ML Internship**.

This project predicts a country's **Human Development Index (HDI)** using important socio-economic indicators such as:

- 🌱 Life Expectancy
- 🎓 Mean Years of Schooling
- 💰 Gross National Income (GNI) per Capita
- 🌐 Internet Users (%)

The application uses a **Linear Regression** model and provides the predicted HDI score along with its corresponding development category.

---
## 🎯 Objective

The objective of this project is to simplify HDI prediction by allowing users to enter a few development indicators and instantly obtain the estimated HDI score and development classification.

---

## ✨ Features

- Predict Human Development Index (HDI)
- Interactive Flask web application
- User-friendly interface
- Machine Learning using Linear Regression
- Predicts HDI score in real time
- Displays HDI category:
  - Very High
  - High
  - Medium
  - Low
- Country selection support

---

🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn (Linear Regression)

### Web Framework
- Flask

### Frontend
- HTML
- CSS
- JavaScript

### Libraries
- Pandas  (Data
- NumPy      processing)
- Matplotlib(Visua
- Seaborn       lization)
- Pickle  (Model serialization)

## 📂 Project Structure

```
HDI_Project/
│
├── Dataset/
│   └── HDI.csv
│
├── Flask/
│   ├── app.py
│   ├── HDI.pkl
│   ├── label_encoder.pkl
│   └── templates/
│       ├── home.html
│       ├── indexnew.html
│       └── resultnew.html
│
├── Training/
│   └── HumDevIndex.py
│
├── README.md
└── requirements.txt
```

---


## Step-by-Step Setup in VS Code

### 1. Install dependencies
Open VS Code terminal and run:

    pip install -r requirements.txt


### 2. Download the dataset
Download HDI.csv from:
    https://github.com/GuidedProjects/HumanDevelopmentIndex/tree/main/Dataset

Place it inside:   HDI_Project/Dataset/HDI.csv


### 3. Train the model
Navigate to the Training folder and run:

    cd Training
    python HumDevIndex.py

This will:
- Load and explore the dataset
- Generate visualizations
- Train the Linear Regression model
- Save HDI.pkl inside the Flask/ folder


### 4. Run the Flask app
Navigate to the Flask folder and run:

    cd Flask
    python app.py

Open your browser and go to:   http://127.0.0.1:5000

---
## 📥 Input Features

The user provides:

- Country
- Life Expectancy
- Mean Years of Schooling
- Gross National Income (GNI) per Capita
- Internet Users (%)

---

## 📈 Output

The application predicts:

- HDI Score
- Development Category
  - Very High Human Development
  - High Human Development
  - Medium Human Development
  - Low Human Development

---


## HDI Tiers

| Score       | Category              |
|-------------|----------------------|
| 0.80 – 0.94 | Very High HDI        |
| 0.70 – 0.80 | High HDI             |
| 0.40 – 0.70 | Medium HDI           |
| 0.30 – 0.40 | Low HDI              |

## 👨‍💻 Team Members

- Rohith Chitteti
- Daggavolu Ganesh
- Yanamala Sreelekha
- Gaddala Amrutha


---

## 🙏 Acknowledgement

This project was developed as part of the **SmartBridge AI & Machine Learning Internship Program**.

---

## 📜 License

This project is created for educational and learning purposes.


