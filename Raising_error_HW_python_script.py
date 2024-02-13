
import numpy as np
import pandas as pd
import openpyxl

# pip install matplotlib

import matplotlib.pyplot as plt

# pip install seaborn

import seaborn as sns


import logging
import argparse

# Create the parser
parser = argparse.ArgumentParser(description="This is a simple script to analyze TTC bus delay data.")

# Add the verbose argument
parser.add_argument('--verbose', action='store_true', help='Enable verbose logging')

# Parse the arguments
args = parser.parse_args()

# Set up logging
if args.verbose:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(description='This is a simple script to analyze TTC bus delay data.')
parser.add_argument('--verbose', '-v', action='store_true', help='Print verbose logs')
args = parser.parse_args()

# Determine logging level based on arguments
logging_level = logging.DEBUG if args.verbose else logging.WARNING

# Initialize logging module
logging.basicConfig(
    level=logging_level, 
    handlers=[logging.StreamHandler(), logging.FileHandler('my_python_analysis.log')],
)

######## elsewhere in your code ########
logging.info('Executing the TTC bus delay analysis script...')



try:
    delay = pd.read_excel('ttc-bus-delay-data-2023.xlsx')
except FileNotFoundError as e:
    e.add_note('Input file is not here, please check the file path again.')
    raise e

delay.head()

delay = pd.DataFrame(delay)

delay.info()

 
# What are the column names?
delay.columns

 
# What are the dtypes when loaded? 
delay.dtypes

 
# How many NaNs are in each column?
delay.isna().sum()

 
# What is the shape of the DataFrame?
delay.shape

 
# For numeric columns: What are the max, min, mean, and median?
print(delay['Min Delay'].max())
print(delay['Min Delay'].min())
print(delay['Min Delay'].mean())
print(delay['Min Delay'].median())

 
# For numeric columns: What are the max, min, mean, and median?
delay.describe()

 
# For text columns: What is the most common value? How many unique values are there?
delay['Route'].unique()


 
delay['Route'].value_counts()

 
delay['Location'].unique()

 
delay['Location'].value_counts()

 
delay['Incident'].unique()

 
delay['Incident'].value_counts()

 
delay = delay.rename(columns=str.lower)

 
delay.columns

 
# Rename one or more columns in the DataFrame
delay = delay.rename(columns={'min delay':'delay_in_min'})
delay = delay.rename(columns={'min gap':'gap_in_min'})

delay.head(3)

 
# Select a single column and find its unique values
delay['incident'].unique()


 
#Select a single text/categorical column and find the counts of its values
delay['incident'].value_counts()

 
# Convert the data type of at least one of the columns
delay.dtypes

 
delay['vehicle'] = delay['vehicle'].astype('int')

 
delay.dtypes

 
delay['vehicle'] = delay['vehicle'].astype('object')

 
delay.dtypes

 
# Write the DataFrame to a different file format than the original
delay.to_csv('delay.csv', index=False)

 
# Create a column derived from an existing one
delay['delay_in_hour'] = round(delay['delay_in_min'] / 60, 2)


 
delay.head(3)

 
delay[['delay_in_min', 'delay_in_hour']].head()

 
# Remove one or more columns from the dataset
delay = delay.drop(columns=['delay_in_hour'])

 
delay.head(3)

 
# Extract a subset of columns and rows to a new DataFrame using .query()
extended_delay = delay.query('delay_in_min > 30')
extended_delay.head()

 
# Extract a subset of columns and rows to a new DataFrame using .loc()
new_delay_data = delay.loc[delay['delay_in_min'] > 30, ['route', 'location', 'incident']]
new_delay_data.head()

 
# Investigate null values
# Create and describe a DataFrame containing records with NaNs in any column
all_null = delay[delay.isna().any(axis=1)].head()

 
# Create and describe a DataFrame containing records with NaNs in a subset of columns
delay.isna().sum()

 
route_null = delay[delay['route'].isna()].head()

 
# If it makes sense to drop records with NaNs in certain columns from the original DataFrame, do so.
route_null = delay.dropna(subset=['route'])

 
route_null.head()

 
# Use groupby() to split your data into groups based on one of the columns
delay.groupby('day')

 
delay.head()

 
# Use agg() to apply multiple functions on different columns and create a summary table. Calculating group sums or standardizing data are two examples of possible functions that you can use
delay.groupby('day').agg({'delay_in_min': 'sum', 'gap_in_min': 'mean'})

 
# Plot two or more columns in your data using matplotlib, seaborn, or plotly
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='delay_in_min', y='gap_in_min', data=delay, hue='day')
plt.title('Delay vs Gap')
plt.xlabel('Delay in Minutes')
plt.ylabel('Gap in Minutes')
plt.show()



 



