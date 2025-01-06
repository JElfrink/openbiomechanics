import pandas as pd

# Read the CSV file
file_path = "C:/Users/jaspe/Documents/GitHub/openbiomechanics/baseball_hitting/data/poi/hittrax.csv"
data = pd.read_csv(file_path)

# Calculate the distribution of pitch_angle
pitch_angle_distribution = data["pitch_angle"].value_counts(normalize=True)

# Print the distribution
print(pitch_angle_distribution)

# Plot the distribution
pitch_angle_distribution.plot(kind="point")