# Program to create a pie chart showing programming language popularity
# Uses matplotlib library for visualization

import matplotlib.pyplot as plt

# Sample data - Programming languages and their popularity percentages
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [30, 25, 20, 25]  # Percentage distribution
colors = ['gold', 'lightblue', 'lightgreen', 'pink']  # Colors for each slice
explode = (0.1, 0, 0, 0)  # Highlight the first slice (Python) by offsetting it

# Create pie chart with specified parameters
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=140)

# Add title and make sure pie is drawn as a perfect circle
plt.title('Programming Language Popularity')
plt.axis('equal')  # Ensures pie is drawn as a circle

# Display the pie chart
plt.show()