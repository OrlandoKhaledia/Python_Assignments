# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading and Exploring the Dataset

try:
    # Load dataset (you can replace with your own CSV path)
    # Example: using Iris dataset from seaborn
    df = sns.load_dataset("iris")
    
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print(" File not found. Please check the dataset path.")
except Exception as e:
    print(" An error occurred while loading the dataset:", e)

# Displaying first few rows

print("\n--- First 5 Rows ---")
print(df.head())

# Dataset information

print("\n--- Dataset Info ---")
print(df.info())

# Check for missing values

print("\n--- Missing Values ---")
print(df.isnull().sum())

# Clean data (if missing values exist)

df = df.dropna()   # Or: df.fillna(value, inplace=True)


# Task 2: Basic Data Analysis

print("\n--- Basic Statistics ---")
print(df.describe())

# Example: Group by species and compute mean petal length

grouped = df.groupby("species")["petal_length"].mean()
print("\n--- Mean Petal Length per Species ---")
print(grouped)

# Interesting finding example
print("\nObservation: Setosa species generally has shorter petals compared to Virginica.")


# Data Visualization

# A. Line chart (using cumulative sum of sepal length as dummy time-series)

df["cumulative_sepal_length"] = df["sepal_length"].cumsum()
plt.figure(figsize=(8,5))
plt.plot(df.index, df["cumulative_sepal_length"], label="Cumulative Sepal Length")
plt.title("Line Chart: Trend of Sepal Length Over Samples")
plt.xlabel("Index")
plt.ylabel("Cumulative Sepal Length")
plt.legend()
plt.show()

# B. Bar chart (average petal length per species)
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal_length", data=df, ci=None)
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length")
plt.show()

# C. Histogram (distribution of sepal length)
plt.figure(figsize=(8,5))
plt.hist(df["sepal_length"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram: Distribution of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

# D. Scatter plot (sepal length vs petal length)
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df)
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend(title="Species")
plt.show()
