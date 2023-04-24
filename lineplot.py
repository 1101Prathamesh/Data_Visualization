import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("tips.csv")

sns.lineplot(x="sex",y="total_bill",data = data)

plt.title("Lineplot")

plt.show()
