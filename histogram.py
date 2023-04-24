import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("tips.csv")


plt.title("Histogram")

plt.hist(data['total_bill'])

plt.show()
