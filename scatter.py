import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns


data = pd.read_csv("tips.csv")

plt.scatter(data['day'],data['tip'])
plt.title("Scatter Plot")
plt.xlabel('day')
plt.ylabel('tip')


plt.show()
