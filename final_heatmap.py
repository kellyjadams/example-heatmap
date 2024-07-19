import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data setup
user_types = ['New Visitors', 'Returning Visitors', 'Subscribers', 'Premium Users']
website_sections = ['Home Page', 'Products Page', 'Blog', 'Support', 'Account Settings']

# Generate realistic data
data = [
    [10, 20, 15, 5, 5],    # New Visitors
    [20, 30, 25, 15, 10],  # Returning Visitors
    [30, 40, 45, 25, 20],  # Subscribers
    [40, 50, 55, 35, 30]   # Premium Users
]

# Create a DataFrame
df = pd.DataFrame(data, index=user_types, columns=website_sections)

# Createthe heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(df, annot=True, cmap='Purples', fmt='d', cbar=False) # Use only one color
plt.title('Website Interaction Heatmap by User Type')
plt.xlabel('Website Section')
plt.ylabel('User Type')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()
