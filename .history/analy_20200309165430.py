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
zf=sz_rent.copy()
zf['perPrice']=sz_rent['price']/sz_rent['size']
#print('PerPrice====',sz_rent['PerPrice'])

# 重新摆放列位置
columns=['Region','form','location','perPrice','price','size','layouts','detail']
zf = pd.DataFrame(zf, columns = columns)

# 重新审视数据集
display(zf.head(n=2))

# 对二手房区域分组对比二手房数量和每平米房价
df_house_count = zf.groupby('Region')['price'].count().sort_values(ascending=False).to_frame().reset_index()
df_house_mean = zf.groupby('Region')['perPrice'].mean().sort_values(ascending=False).to_frame().reset_index()

f, [ax1,ax2,ax3] = plt.subplots(3,1,figsize=(20,15))
sns.barplot(x='Region', y='perPrice', palette="Blues_d", data=df_house_mean, ax=ax1)
ax1.set_title('price',fontsize=15)
ax1.set_xlabel('区域')
ax1.set_ylabel('每平米单价')

sns.barplot(x='Region', y='price', palette="Greens_d", data=df_house_count, ax=ax2)
ax2.set_title('北京各大区二手房数量对比',fontsize=15)
ax2.set_xlabel('区域')
ax2.set_ylabel('数量')

sns.boxplot(x='Region', y='price', data=zf, ax=ax3)
ax3.set_title('北京各大区二手房房屋总价',fontsize=15)
ax3.set_xlabel('区域')
ax3.set_ylabel('房屋总价')

plt.show()
