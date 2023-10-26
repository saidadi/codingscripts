'''
The purpose of this script is to offer a data type analysis and summary for a dataset that is derived from a CSV file.
To import the data, compute summary statistics, and identify the different types of attributes in the data,
it makes use of the Pandas library. The count of characteristics in each use case, the number of use cases in the dataset,
the data types, and the data summary are all output by the code. 
It is a helpful first step toward comprehending the features and organization of the dataset.
Kindly substitute the file path of the dataset you are utilizing for "Electric_Vehicle_Population_Data.csv."
'''

import pandas as pd
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")
dfsummary = df.describe()
dfdatatypes = df.dtypes
uccount = len(dfsummary)
attributecounts = [len(dfsummary[i]) for i in dfsummary]
print("Data Summary:")
print(dfsummary)
print("\nData Types:")
print(dfdatatypes)
print(f"\nUse Cases: {uccount}")
print(f"No of Attributes in Particular Use Case: {attributecounts}")
