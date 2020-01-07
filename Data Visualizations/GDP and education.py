import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
import numpy as np

GDP = pd.read_excel('GDP.xlsx')
GDP = GDP.drop(index=0)
GDP = GDP[::-1]

topuni = pd.read_excel('topuni.xlsx')
topuni = topuni.drop(index=0)
topuni = topuni[::-1]

gdp = GDP['GDP'].tolist()
uni = topuni['Number of Top 100 Universities'].tolist()
diff = [abs(i-1000000*j) for i in gdp for j in uni]
color = [cm.Greens(abs(x)) if x>=np.mean(diff) else cm.Reds(abs(x)) for x in diff]
    
plt.figure(1, figsize=(12,12))

linegraph = plt.plot(GDP['Provinces'],GDP['GDP'],'-o')
bargraph = plt.bar(topuni['Provinces'],height = topuni['Number of Top 100 Universities']*1000000, color=color,alpha=0.5)

for bar in bargraph:
    height = bar.get_height()
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height()*0.8, str(int(height)/1000000), 
                 ha='center', color='w', fontsize=8)

plt.xticks(rotation=270)
plt.ticklabel_format(style='plain', axis='y')#avoid scientific format

plt.xlabel('Provinces')
plt.ylabel('GDP(CNY¥)')
plt.title('The GDP of privinces in China in 2018 and the number of Top 100 Universities in each province')

plt.show()
