import pandas as pd

data={'date': ['1/1/20', '1/2/20', '1/3/20', '1/4/20', '1/5/20', '1/6/20', '1/7/20', '1/8/20', '1/9/20', '1/10/20'],
    'was_rainy':[False,True,True,False,False,True,False,True,True, True]}
i=[] #index
df=pd.DataFrame(data)
print(df) #Datos originales
for n in df.index:
    if df.iloc[n]['was_rainy']==False:
        if df.iloc[n+1]['was_rainy']==True:
            i.append(n+1)
        else:
            pass
    else: 
        pass

print (df.loc[i]) #Salida
print (df.loc[i].to_html())
