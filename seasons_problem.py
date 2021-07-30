import pandas as pd
from datetime import datetime 

data={'ORD-ID':['113-8909896-6940269', '114-0291773-7262677', '114-0291773-7262697',
                '114-9900513-7761000', '112-5230502-8173028', '112-7714081-3300254',
                '114-5384551-1465853', '114-7232801-4607440'],
     'ORD_DT':['9/23/19', '1/1/20', '12/5/19', '9/24/20', '1/30/20', '5/2/20', '4/2/20',
               '10/9/20'],
     'QT_ORDD':['1','1','1','1','1','1','1','1']}


df=pd.DataFrame(data)
print(df)
df['ORD_DT']=pd.to_datetime(df['ORD_DT'])
bucle=df.index
seasons=[]
n=0
#Spring: March 19th - June 19th  319 - 619
#Summer: June 20th - September 21st 620 - 921
#Fall: September 22nd - December 20th 922 - 1220
#Winter: December 21th - March 18th 1221 - 318
fecha = df['ORD_DT'].dt.strftime("%m%d")
aux= [int(x) for x in fecha]
print ('-------------------------------------------')
for n in bucle:
    if (aux[n]>= 319 and aux[n]<= 619):
        seasons.append('Spring')
    elif (aux[n]>= 620 and aux[n]<= 921):
        seasons.append('Summer')
    elif (aux[n]>= 922 and aux[n]<= 1220):
        seasons.append('Fall')
    else:
        seasons.append('Winter')
df2=df.drop(['ORD_DT', 'QT_ORDD'], axis=1)
df2['SEASON']= seasons
print(df2)
print(df2.to_html())
