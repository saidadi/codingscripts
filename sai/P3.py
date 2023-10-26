'''
The code that is provided analyzes a dataset pertaining to electric vehicles using exploratory data analysis, or EDA. The dataset is loaded first, then its structure is examined. To guarantee data completeness, null values are checked and rows with null values in the "County," "Legislative District," and "Vehicle Location" columns are eliminated.
The code then uses Matplotlib and Seaborn for comparison to create histograms for different properties. Postal code, model year, electric range, base MSRP, legislative district, DOL vehicle ID, and 2020 census tract are among the data sets for which histograms are made.
Understanding the distribution of each attribute within the dataset is made easier with the aid of these visualizations, which also shed light on possible trends and other features of the data.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Electric_Vehicle_Population_Data.csv")

df.head()

df.isnull().sum()



df.info()

df.describe()

df.dropna(subset=['County'], inplace=True)

df.dropna(subset=['Legislative District'], inplace=True)

df.dropna(subset=['Vehicle Location'], inplace=True)

df.isnull().sum()

plt.figure(figsize=(8, 6))
plt.hist(df['Postal Code'], bins=20, edgecolor='k')
plt.title('Histogram of Postal Code (Matplotlib)')
plt.xlabel('Postal Code')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(8, 6))
sns.histplot(df['Postal Code'], bins=20, kde=True)
plt.title('Histogram of Postal Code (Seaborn)')
plt.xlabel('Postal Code')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(df['Model Year'], bins=20, edgecolor='k')
plt.title('Histogram of Model Year (Matplotlib)')
plt.xlabel('Model Year')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(df['Model Year'], bins=20, kde=True)
plt.title('Histogram of Model Year (Seaborn)')
plt.xlabel('Model Year')
plt.ylabel('Frequency')
plt.show()



plt.figure(figsize=(8, 6))
plt.hist(df['Electric Range'], bins=20, edgecolor='k')
plt.title('Histogram of Electric Range (Matplotlib)')
plt.xlabel('Electric Range')
plt.ylabel('Frequency')
plt.show()




plt.figure(figsize=(8, 6))
sns.histplot(df['Electric Range'], bins=20, kde=True)
plt.title('Histogram of Electric Range (Seaborn)')
plt.xlabel('Electric Range')
plt.ylabel('Frequency')
plt.show()



plt.figure(figsize=(8, 6))
plt.hist(df['Base MSRP'], bins=20, edgecolor='k')
plt.title('Histogram of Base MSRP (Matplotlib)')
plt.xlabel('Base MSRP')
plt.ylabel('Frequency')
plt.show()



plt.figure(figsize=(8, 6))
sns.histplot(df['Base MSRP'], bins=20, kde=True)
plt.title('Histogram of Base MSRP (Seaborn)')
plt.xlabel('Base MSRP')
plt.ylabel('Frequency')
plt.show()



plt.figure(figsize=(8, 6))
plt.hist(df['Legislative District'], bins=20, edgecolor='k')
plt.title('Histogram of Legislative District (Matplotlib)')
plt.xlabel('Legislative District')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(8, 6))
sns.histplot(df['Legislative District'], bins=20, kde=True)
plt.title('Histogram of Legislative District (Seaborn)')
plt.xlabel('Legislative District')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(8, 6))
plt.hist(df['DOL Vehicle ID'], bins=20, edgecolor='k')
plt.title('Histogram of DOL Vehicle ID (Matplotlib)')
plt.xlabel('DOL Vehicle ID')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(8, 6))
sns.histplot(df['DOL Vehicle ID'], bins=20, kde=True)
plt.title('Histogram of DOL Vehicle ID (Seaborn)')
plt.xlabel('DOL Vehicle ID')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(8, 6))
plt.hist(df['2020 Census Tract'], bins=20, edgecolor='k')
plt.title('Histogram of 2020 Census Tract (Matplotlib)')
plt.xlabel('2020 Census Tract')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(8, 6))
sns.histplot(df['2020 Census Tract'], bins=20, kde=True)
plt.title('Histogram of 2020 Census Tract (Seaborn)')
plt.xlabel('2020 Census Tract')
plt.ylabel('Frequency')
plt.show()



