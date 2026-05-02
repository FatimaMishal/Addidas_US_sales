
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=df = pd.read_excel('/content/Adidas US Sales Datasets.xlsx')
df.head(10)

df = df.iloc[3:]
df = df.reset_index(drop=True)
df.head(10)

df = df.drop(df.columns[0], axis=1)
df.shape

df.columns = ['Retailer', 'Retailer ID', 'Invoice Date','Region','State','City','Product','Price per Unit','Units Sold','Total Sales','Operating Profit','Operating Margin','Sales Method']

df = df.iloc[1:].copy()
df = df.reset_index(drop=True)

df.isnull().sum()

df.info()

df['Operating Margin'] = pd.to_numeric(df['Operating Margin'], errors='coerce')
df['Operating Margin'] = df['Operating Margin'].astype(float)

df.info()

cols = ['Price per Unit', 'Units Sold', 'Total Sales','Operating Profit']
df[cols] = df[cols].astype(int)
print(df.dtypes)

df.head(3)

df.duplicated().sum()

product_sales = df.groupby('Product')['Units Sold'].sum().sort_values(ascending=False)
display(product_sales.head(1))

sales_by_region = df.groupby('Region')['Total Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=sales_by_region.index, y=sales_by_region.values, hue=sales_by_region.index, palette='viridis', legend=False)
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

df['Invoice Date'] = pd.to_datetime(df['Invoice Date'])
daily_sales = df.groupby('Invoice Date')['Total Sales'].sum().reset_index()

plt.figure(figsize=(14, 7))
sns.lineplot(x='Invoice Date', y='Total Sales', data=daily_sales)
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df['Month'] = df['Invoice Date'].dt.month
monthly_sales = df.groupby('Month')['Total Sales'].sum().sort_values(ascending=False)
display(monthly_sales.head())

sales_method_by_month = df.pivot_table(index='Month', columns='Sales Method', values='Total Sales', aggfunc='sum')
display(sales_method_by_month.head())

df['Year'] = df['Invoice Date'].dt.year
yearly_sales = df.groupby('Year')['Total Sales'].sum().sort_values(ascending=False)
display(yearly_sales)

plt.figure(figsize=(8, 5))
sns.barplot(x=yearly_sales.index, y=yearly_sales.values, hue=yearly_sales.index, palette='viridis', legend=False)
plt.title('Total Sales by Year')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

retailer_sales = df.groupby('Retailer')['Total Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=retailer_sales.index, y=retailer_sales.values, hue=retailer_sales.index, palette='viridis', legend=False)
plt.title('Total Sales by Retailer')
plt.xlabel('Retailer')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 10))
plt.pie(sales_by_region.values, labels=sales_by_region.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', len(sales_by_region)))
plt.title('Total Sales Distribution by Region')
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()





print(df['Sales Method'].unique())

sales_by_method = df.groupby('Sales Method')['Total Sales'].sum().sort_values(ascending=False)
display(sales_by_method)

plt.figure(figsize=(8, 6))
sns.barplot(x=sales_by_method.index, y=sales_by_method.values, hue=sales_by_method.index, palette='crest', legend=False)
plt.title('Total Sales by Sales Method')
plt.xlabel('Sales Method')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()