# Program to convert pandas Series to a Python list
# Demonstrates the tolist() method of pandas Series

import pandas as pd

# Create a pandas Series with sample data
seriesData = pd.Series([10, 20, 30, 40, 50])

# Convert the Series to a Python list
listData = seriesData.tolist()

# Display the converted list and its data type
print("Python List:", listData) 
print("Type:", type(listData))