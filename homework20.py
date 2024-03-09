# Numpy

import numpy as np


zeros_array = np.zeros((4, 3))
print("Array of all zeros:")
print(zeros_array)
print()


ones_array = np.ones((4, 3))
print("Array of all ones:")
print(ones_array)
print()


numbers_array = np.arange(12).reshape(4, 3)
print("Array of numbers from 0 to 11:")
print(numbers_array)
print()


x_values = np.arange(1, 101, 1)
f_x_values = 2 * x_values ** 2 + 5
print("Tabulation of F(x) = 2x^2 + 5 for x in [1, 100] with step 1:")
print("x\t|\tF(x)")
for x, f_x in zip(x_values, f_x_values):
    print(f"{x}\t|\t{f_x}")


x_values = np.arange(-10, 11, 1)
f_x_values = np.exp(-x_values)
print("\nTabulation of F(x) = e^(-x) for x in [-10, 10] with step 1:")
print("x\t|\tF(x)")
for x, f_x in zip(x_values, f_x_values):
    print(f"{x}\t|\t{f_x}")

# Pandas

import pandas as pd

df = pd.read_csv("temp.csv")


selected_columns = df[['Team', 'Yellow Cards', 'Red Cards']]


num_teams = selected_columns['Team'].nunique()


filtered_teams = df[df['Goals'] > 6]

print("Number of teams participated in the Euro2012:", num_teams)
print("Teams that scored more than 6 goals:")
print(filtered_teams[['Team', 'Goals']])

# DataViz

import seaborn as sns
import matplotlib.pyplot as plt

tips_df = sns.load_dataset("tips")
iris_df = sns.load_dataset("iris")

# Bar Plot
sns.barplot(x="day", y="total_bill", data=tips_df)
plt.title("Average Total Bill by Day")
plt.show()

# Count Plot
sns.countplot(x="day", data=tips_df)
plt.title("Count of Observations by Day")
plt.show()

# Histogram
sns.histplot(data=iris_df, x="petal_length")
plt.title("Distribution of Petal Length")
plt.show()

# Box Plot
sns.boxplot(x="species", y="petal_length", data=iris_df)
plt.title("Distribution of Petal Length by Species")
plt.show()

# Violin Plot
sns.violinplot(x="species", y="petal_length", data=iris_df)
plt.title("Distribution of Petal Length by Species")
plt.show()

# Scatter Plot
sns.scatterplot(x="sepal_length", y="sepal_width", data=iris_df)
plt.title("Relationship between Sepal Length and Sepal Width")
plt.show()
