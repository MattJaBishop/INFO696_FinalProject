import matplotlib.pyplot as plt
import pandas as pd

headers = ['Year', 'Cost in Billions']

df = pd.read_csv('NationalHealthExpenditures_BillionDollarsTest.csv', delimiter=",", names=headers)
x = df['Year']
y = df['Cost in Billions']

plt.bar(x, y)
plt.xlabel('Year')
plt.ylabel('Cost in Billions')
plt.title('National Health Expenture Totals by Year')
plt.show()