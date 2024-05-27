import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read the CSV file
df = pd.read_csv("householdtask3.csv")
print(df.head())

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['year'], df['own'], color='blue', label='Ownership Rate')
plt.title("Ownership Rate by Year")
plt.xlabel('Year')
plt.ylabel('Ownership Rate')
plt.legend()
plt.grid(True)
plt.show()

# Bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['year'], df['own'], color='green', label='Ownership Rate')
plt.title("Bar Plot of Ownership Rate by Year")
plt.xlabel('Year')
plt.ylabel('Ownership Rate')
plt.legend()
plt.show()

# Line chart
plt.figure(figsize=(10, 6))
plt.plot(df['year'], df['own'], color='red', marker='o', linestyle='-', label='Ownership Rate')
plt.title("Line Chart of Ownership Rate by Year")
plt.xlabel('Year')
plt.ylabel('Ownership Rate')
plt.legend()
plt.grid(True)
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(df['income'], bins=20, color='purple', edgecolor='black', label='Income Distribution')
plt.title("Histogram of Income")
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.legend()
plt.show()
