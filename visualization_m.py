import pandas as pd
import matplotlib.pyplot as plt

# TODO: Load dataset; replace this csv to your file
df = pd.read_csv("Data/US_Accidents_March23.csv")

# Step 1: Handling the format
# TODO: Remove extra precision if exists

# TODO: Extract relevant time-based features

# TODO: Fix missing values for numerical columns

# TODO: Ensure Severity is numeric
df['Severity'] = pd.to_numeric(df['Severity'], errors='coerce')
df = df.dropna(subset=['Severity'])



severity_counts = df['Severity'].value_counts(normalize=True) * 100
my_labels = severity_counts.index

# Pie Charts
# plt.pie(severity_counts,labels=my_labels)
# plt.show()

# Bar Charts 
plt.bar(my_labels, severity_counts)
plt.xlabel("Severity Level")
plt.ylabel("Count")
plt.show()



# # Road conditions presence
# road_conditions = ['Crossing', 'Traffic_Signal', 'Junction']
# for condition in road_conditions:
    

# Bar Plots
# # Accident Cases vs Hours
# hourly_counts = df['Hour'].value_counts().sort_index()


# Accident Cases vs Months


# Accident Cases vs Different Temperature


# Accident Cases vs Different Humidity


# Accident Cases vs Wind Speed
