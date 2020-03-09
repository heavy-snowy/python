import pandas as pd

#合并不同的爬虫数据表格
renting=[]
renting.append(pd.read_csv('total.csv',delimiter=':',header=None))
renting.append(pd.read_csv('rent.csv',delimiter=':',header=None))
print('========================')
nf=pd.concat(renting)

nf.to_csv('total.csv',header=None,index=False,sep=':')

#写入表头
columns=['title','price','layout','address','agent','href']
df = pd.read_csv('total.csv',header=0,names=columns)
#去重
datalist = df.drop_duplicates()
datalist.to_csv('distinct.csv',index=False)
#表格的拆分
un_df=pd.read_csv('distinct.csv',header=0)
un_df['size_unit'] = un_df['layout'].str.extract('(\d+㎡)')
un_df['size'] = un_df['size_unit'].str.extract('(\d{1,})')
un_df['form'], un_df['detail'] = un_df['title'].str.split('|', 1).str

un_df['Region'], un_df['location']  =un_df['address'].str.split('  ',1).str
un_df['layouts']  =un_df['layout'].str.split('    ',1).str[0]
#表头列的删除
del_columns=['title','layout','address','agent']
un_df=un_df.drop(del_columns,axis=1)
#表头列的排序
order = ['Region','form','location','price','size','layouts','detail','href']
un_df = un_df[order]

un_df.to_csv('merge_zc.csv')



