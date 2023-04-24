import pandas as pd
import matplotlib.pyplot as plt
import seaborn  as sns


data = pd.read_csv("tips.csv")

plt.bar(data['day'], data['tip'])
 
plt.title("Bar Chart")
 

plt.xlabel('Day')
plt.ylabel('Tip')
 

plt.show()
