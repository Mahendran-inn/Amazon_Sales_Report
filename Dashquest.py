#Load the Dataset using pandas
import pandas as pd

data=pd.read_csv('Amazon Sale Report - Amazon Sale Report.csv.csv')
df=data.copy()

#check null probability
proba_nulls=df.isnull().mean()*100

#drop unwanted column
df=df.drop(columns=['Unnamed: 22','fulfilled-by'],axis=1)

#fill columns with neccessary points
df['ship-postal-code']=df['ship-postal-code'].fillna(0).astype('int32').astype(str)
df['Amount']=df['Amount'].fillna(0)
df['currency']=df['currency'].fillna('INR')
df['ship-city']=df['ship-city'].fillna('Unknown')
df['ship-state']=df['ship-state'].fillna('Unknown')
df['ship-country']=df['ship-country'].fillna('Unknown')
df['Amount']=df['Amount'].fillna('Unknown')
df['promotion-ids']=df['promotion-ids'].fillna(df['promotion-ids'].mode()[0])

#feature extraction by date,month,year
df['Date']=pd.to_datetime(df['Date'],errors='coerce')
df['day']=df['Date'].dt.day
df['month']=df['Date'].dt.month
df['year']=df['Date'].dt.year

#find and replace
df.loc[df['Courier Status'].isna() & (df['Qty']>=1),'Courier Status'] = 'Shipped'
df.loc[df['Courier Status'].isna() & (df['Qty']==0),'Courier Status'] = 'Cancelled'

#conversion of cleaned dataframe into csv file
df.to_csv('Amazon_cleaned_dataset.csv',index=False)
