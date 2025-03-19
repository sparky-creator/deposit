import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("QueryResults.csv", names=['Date', 'Tag', 'Post'])
print(data.info())

new_data = data.pivot(index = "Date", columns ="Tag", values = "Post")

plt.plot(new_data.index, new_data.python)
plt.show()

