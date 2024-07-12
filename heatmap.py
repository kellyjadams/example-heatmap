import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data setup
user_types = ['New Visitors', 'Returning Visitors', 'Subscribers', 'Premium Users']
website_sections = ['Home Page', 'Products Page', 'Blog', 'Support', 'Account Settings']

# Generate random data: each cell represents the duration or number of interactions of users in a section
data = np.random.randint(0, 100, size=(len(user_types), len(website_sections)))

# Create a DataFrame for better handling
df = pd.DataFrame(data, index=user_types, columns=website_sections)

# Creating the heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(df, annot=True, cmap='viridis', fmt='d')
plt.title('Website Interaction Heatmap by User Type')
plt.xlabel('Website Section')
plt.ylabel('User Type')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()
