import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# load karo file ko
df = pd.read_csv("Netflix_dataset.csv")

# see the first five coloumn
print(df.head())

# lets understand the dataset

# shape of dataset

print("Rows and columns",df.shape)
# stats using describe

print(df.describe(include="all"))

# data typpes

print(df.dtypes)

# check the null values
print("\nCheck the null values\n")
print(df.isnull().sum())

# drop the rows with missing values

df_cleaned = df.dropna()

# fill missing values with placeholder
df.fillna("Not Avialable" , inplace=True)

print(df_cleaned.shape)

print(df_cleaned.isnull().sum())

# How many movies vs TV Shows?
print(df_cleaned['type'].value_counts())


print(df_cleaned['country'].value_counts().head(5))

df_cleaned['type'].value_counts().plot(kind='bar', title='Content Type')
plt.show()