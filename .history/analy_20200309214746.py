import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import re
import matplotlib.pyplot as plt
from matplotlib.font_manager import _rebuild
from IPython.display import display

# plt.style.use("fivethirtyeight")
# sns.set_style({'font.sans-serif':['simhei','Arial']})
plt.rcParams['font.sans-serif']=['simHei'] #用来正常显示中文标签 

plt.rcParams['font.size'] = 6
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# 导入数据
sz_rent = pd.read_csv('merge_zc.csv')
# print('data-row2====')
display(sz_rent.head(n=2))

_rebuild() #reload一下

# # 检查缺失值情况
# print('info====')
sz_rent.info()

print('describe====')
print(sz_rent.describe())

# 添加新特征均价
zf=sz_rent.copy()
zf['perPrice']=sz_rent['price']/sz_rent['size']
#print('PerPrice====',sz_rent['PerPrice'])

# # 重新摆放列位置
columns=['Region','form','location','perPrice','price','size','layouts','detail']
zf = pd.DataFrame(zf, columns = columns)

# # 重新审视数据集
display(zf.head(n=2))

size={'size',10}

# # 对二手房区域分组对比二手房数量和每平米房价
df_house_count = zf.groupby('Region')['price'].count().sort_values(ascending=False).to_frame().reset_index()
df_house_mean = zf.groupby('Region')['perPrice'].mean().sort_values(ascending=False).to_frame().reset_index()

f, [ax1,ax2,ax3] = plt.subplots(3,1,figsize=(20,15))
sns.barplot(x='Region', y='perPrice', palette="Blues_d", data=df_house_mean, ax=ax1)
ax1.set_title('深圳各个区域的每平方米的租金对比',fontsize=15)
ax1.set_xlabel('region',rotation=80,fontsize=1)
ax1.set_ylabel('unit price')

sns.barplot(x='Region', y='price', palette="Greens_d", data=df_house_count, ax=ax2)
ax2.set_title('深圳各个区域的月租对比',fontsize=15)
ax2.set_xlabel('region')
ax2.set_ylabel('quantity')

sns.boxplot(x='Region', y='price', data=zf, ax=ax3)
ax3.set_title('深圳各个区域的租金箱型图对比',fontsize=15)
ax3.set_xlabel('region')
ax3.set_ylabel('total price')

plt.show()
