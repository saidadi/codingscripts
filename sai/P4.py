'''
This code uses an Electric_Vehicle_Population_Data dataset to do exploratory data analysis (EDA). After importing the dataset, the EDA chooses a subset of information pertinent to the study, paying particular attention to the attributes "Make," "Model," and "Electric Range." It eliminates rows with missing values to guarantee the completeness of the data.
The code then uses Seaborn and Matplotlib to build scatterplots that show the electric range distribution by vehicle make. The scatterplots, which have an alpha of 0.3 to accommodate for overlapping spots, shed light on how the electric range varies amongst various car makes.
We can potentially identify patterns or trends in the data by using this analysis to better understand the relationship between the 'Make' and 'Electric Range' parameters. 

'''


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Electric_Vehicle_Population_Data.csv')

# Subset the data for analysis
subset_df = df[['Make', 'Model', 'Electric Range']]

# Filter out rows with missing values
subset_df = subset_df.dropna()

# Create a scatterplot to visualize the distribution of electric range by make using Matplotlib
plt.figure(figsize=(10, 6))
plt.title("Electric Range by Vehicle Make (Matplotlib)")
plt.scatter(subset_df['Make'], subset_df['Electric Range'], alpha=0.3)
plt.xlabel("Make")
plt.ylabel("Electric Range (miles)")
plt.xticks(rotation=90)
plt.show()

# Create a scatterplot to visualize the distribution of electric range by make using Seaborn
plt.figure(figsize=(10, 6))
plt.title("Electric Range by Vehicle Make (Seaborn)")
sns.scatterplot(data=subset_df, x='Make', y='Electric Range', alpha=0.3)
plt.xlabel("Make")
plt.ylabel("Electric Range (miles)")
plt.xticks(rotation=90)
plt.show()

