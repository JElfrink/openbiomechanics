# File to find the amount of entries per session in poi_metrics.csv

import pandas as pd
#import matplotlib.pyplot as plt

# Read the CSV file
file_path = "C:/Users/jaspe/Documents/GitHub/openbiomechanics/baseball_pitching/data/poi/poi_metrics.csv"
data = pd.read_csv(file_path)

# Group the data by session and count the amount of entries per session
grouped_data = data.groupby('session').size()

# Print the result with highest count first
grouped_data = grouped_data.sort_values(ascending=False)
print(grouped_data)
#print(grouped_data)

# Create a historgram for the count of entries per session
#plt.hist(grouped_data)

