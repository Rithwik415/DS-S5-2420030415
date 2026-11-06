
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

df = sns.load_dataset("iris")

print("First 5 rows:\n", df.head())
print("\nDimensions:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nData types:\n", df.dtypes)
print("\nSummary statistics:\n", df.describe())

x = df["sepal_length"]

print("\nMean:", x.mean())
print("Median:", x.median())
print("Mode:", x.mode()[0])
print("Variance:", x.var())
print("Standard Deviation:", x.std())
print("Range:", x.max() - x.min())
print("Skewness:", skew(x))
print("Kurtosis:", kurtosis(x))

plt.hist(x, bins=10, edgecolor="black")
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()
sns.boxplot(x=x)
plt.title("Boxplot of Sepal Length")
plt.show()

df["species"].value_counts().plot.pie(autopct="%1.1f%%")
plt.title("Species Distribution")
plt.ylabel("")
plt.show()

sns.scatterplot(data=df, x="sepal_length",y="petal_length", hue="species")
plt.title("Sepal Length vs Petal Length")
plt.show()
sns.barplot(data=df, x="species", y="petal_length")
plt.title("Average Petal Length by Species")
plt.show()
sns.heatmap(df.select_dtypes(include="number").corr(),annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
sns.pairplot(df, hue="species")
plt.show()
sns.violinplot(data=df, x="species", y="petal_length")
plt.title("Petal Length Across Species")
plt.show()
print("\nOBSERVATIONS")
print("1. Setosa has smaller petals than the other species.")
print("2. Petal length differs among the three species.")
print("3. Sepal length and petal length are positively correlated.")

print("\nEDA completed successfully.")
