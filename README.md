# ML-0027 Human Development Index Prediction
# =============================================

## Project Structure

HDI_Project/
├── Dataset/
│   └── HDI.csv                  ← Place your dataset here
├── Flask/
│   ├── app.py                   ← Flask web application
│   ├── HDI.pkl                  ← Generated after training
│   └── templates/
│       ├── home.html
│       ├── indexnew.html
│       └── resultnew.html
├── Training/
│   └── HumDevIndex.py           ← Run this first to train the model
└── requirements.txt


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

    cd ../Flask
    python app.py

Open your browser and go to:   http://127.0.0.1:5000


## HDI Tiers

| Score       | Category              |
|-------------|----------------------|
| 0.80 – 0.94 | Very High HDI        |
| 0.70 – 0.80 | High HDI             |
| 0.40 – 0.70 | Medium HDI           |
| 0.30 – 0.40 | Low HDI              |


## Tech Stack
- Python 3.10+
- Flask (web framework)
- Scikit-learn (Linear Regression)
- Pandas / NumPy (data processing)
- Matplotlib / Seaborn (visualization)
- Pickle (model serialization)
