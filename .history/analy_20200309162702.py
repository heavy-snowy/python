import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import re
import matplotlib.pyplot as plt
from IPython.display import display
plt.style.use("fivethirtyeight")
sns.set_style({'font.sans-serif':['simhei','Arial']})


# 导入数据
sz_rent = pd.read_csv('merge_zc.csv')
print('data-row2====')
display(sz_rent.head(n=2))

# 检查缺失值情况
print('info====')
sz_rent.info()

print('describe====')
sz_rent.describe()

# 添加新特征均价
rent=sz_rent.copy()
rent['perPrice']=sz_rent['price']/sz_rent['size']
#print('PerPrice====',sz_rent['PerPrice'])

# 重新摆放列位置
columns=['Region','form','location','perPrice','price','size','layouts','detail']
rent = pd.DataFrame(rent, columns = columns)

# 重新审视数据集
display(rent.head(n=2))
