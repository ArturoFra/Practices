import pandas as pd

data={'order_number':[ 1567, 1567, 1567, 1234, 1234, 1234, 9834, 9834, 7654, 7654],
    'item_name': ['LAPTOP', 'MOUSE', 'KEYBOARD', 'GAME', 'BOOK', 'BOOK', 'SHIRT', 'PANTS', 'TV', 'DVD'],
    'status': ['SHIPPED', 'SHIPPED', 'PENDING', 'SHIPPED', 'CANCELLED', 'CANCELLED', 'SHIPPED', 'CANCELLED', 'CANCELLED', 'CANCELLED']}
i=[]
d=[]
df=pd.DataFrame(data)
print(df)
n=1
df2 = df.drop_duplicates(['order_number', 'status'], keep='last').reset_index()
for n in df2.index:
    
    if df2.iloc[n]['order_number'] == df2.iloc[n-1]['order_number']:
        if df2.iloc[n]['status']=='SHIPPED' and df2.iloc[n-1]['status']=='SHIPPED' or df2.iloc[n]['status']=='SHIPPED' and df2.iloc[n-1]['status']=='CANCELLED'or df2.iloc[n]['status']=='CANCELLED' and df2.iloc[n-1]['status']=='SHIPPED':
            i.append('SHIPPED')
        elif df2.iloc[n]['status']=='SHIPPED' and df2.iloc[n-1]['status']=='PENDING' or df2.iloc[n]['status']=='PENDING' and df2.iloc[n-1]['status']=='SHIPPED'or df2.iloc[n]['status']=='CANCELLED' and df2.iloc[n-1]['status']=='PENDING'or df2.iloc[n]['status']=='PENDING' and df2.iloc[n-1]['status']=='CANCELLED':
            i.append('PENDING')
        elif df2.iloc[n]['status']=='CANCELLED' and df2.iloc[n]['status']=='CANCELLED':
            i.append('CANCELLED')
        else : 
            pass
    elif(df2.iloc[n]['status']=='CANCELLED'):
            i.append('CANCELLED')
            d.append(n)
    else:
            d.append(n)
            pass
 
res=df2.loc[d].drop(['item_name', 'status','index'], axis=1).reset_index(drop=True)
res['status']=i
print(res)
print(res.to_html())
       


