# ============================================================
#  Human Development Index - Model Training
#  Run this file FIRST to generate HDI.pkl
# ============================================================

# Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Step 2: Load Dataset
Development = pd.read_csv("Dataset/HDI.csv")
print("Dataset shape:", Development.shape)
print(Development.head())

# Step 3: Explore Dataset
print("\nColumn names:")
print(Development.columns.tolist())

print("\nUnique countries:", Development["Country"].nunique())
print(Development["Country"].unique())

# Step 4: Data Visualization (first 20 rows)
data1 = Development.head(20)

# Plot 1: Mean Years of Schooling vs HDI
plt.figure(figsize=(8, 5))
g = sns.stripplot(x="Mean years of schooling", y="HDI", data=data1, jitter=True)
plt.xticks(rotation=90)
plt.title("Mean Years of Schooling vs HDI")
plt.tight_layout()
plt.savefig("Dataset/plot_schooling_vs_hdi.png")
plt.close()

# Plot 2: Life Expectancy vs HDI
plt.figure(figsize=(8, 5))
g = sns.stripplot(x="Life expectancy", y="HDI", data=data1, jitter=True)
plt.xticks(rotation=90)
plt.title("Life Expectancy vs HDI")
plt.tight_layout()
plt.savefig("Dataset/plot_life_vs_hdi.png")
plt.close()

# Plot 3: Correlation Heatmap
# Plot 3: Correlation Heatmap
heat = Development[[
    "HDI",
    "Life expectancy",
    "Mean years of schooling",
    "GNI per capita",
    "Internet users"
]]

plt.figure(figsize=(8, 6))
sns.heatmap(heat.corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("Dataset/plot_heatmap.png")
plt.close()
# Step 5: Select Features (Independent & Dependent Variables)
# Columns: Country(2), Life expectancy(5), Mean years of schooling(6),
#          GNI per capita(7), Internet users(67)
X = Development.iloc[:, [2, 5, 6, 7, 67]]
X = pd.DataFrame(X)

y = Development.iloc[:, 4].values   # HDI column
y = pd.DataFrame(y)

print("\nX shape:", X.shape)
print("y shape:", y.shape)

# Step 6: Handle Null Values
print("\nNull values in X:")
print(X.isnull().sum())

X.fillna(X.mean(numeric_only=True), inplace=True)

print("\nNull values after filling:")
print(X.isnull().sum())

# Step 7: Label Encoding for Country column
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X["Country"] = le.fit_transform(X["Country"].astype(str))
with open("Flask/label_encoder.pkl", "wb") as f:
    pickle.dump(le, f)

# Step 8: Train / Test Split (90% train, 10% test)
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42
)
print("\nTraining samples:", x_train.shape[0])
print("Testing  samples:", x_test.shape[0])

# Step 9: Fit Linear Regression Model
reg = LinearRegression()
reg.fit(x_train, y_train)
print("\nModel trained successfully.")

# Step 10: Predict & Evaluate
y_pred = reg.predict(x_test)
print("\nPredicted values:")
print(y_pred)

r2 = r2_score(y_test, y_pred)
print(f"\nR² Score: {r2:.4f}")

# Quick test with sample values
# Quick test with sample values
sample_df = pd.DataFrame({
    "Country": [13],
    "Life expectancy": [72.0],
    "Mean years of schooling": [5.2],
    "GNI per capita": [3341.0],
    "Internet users": [14.4]
})

sample = reg.predict(sample_df)
print(f"\nSample prediction: {round(sample[0][0], 2)}")

# Step 11: Save Model as Pickle
with open("Flask/HDI.pkl", "wb") as f:
    pickle.dump(reg, f)

print("\nModel saved as Flask/HDI.pkl — ready for deployment!")
