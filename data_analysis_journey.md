# Customer Shopping Behavior Analysis

This notebook documents my data analysis journey as I explored a customer shopping dataset, cleaned the data, and created new features for analysis.

## 1. Import the library
```python
import pandas as pd
```

## 2. Load the dataset
```python
df = pd.read_csv("customer_shopping_behavior.csv")
print(df.head())
```

## 3. Understand the structure of the data
```python
df.info()
df.describe(include='all')
```

## 4. Check for missing values
```python
df.isnull().sum()
```

## 5. Fill missing review ratings by category
```python
# Fill missing review ratings using the median rating for each product category
# This helps keep the data useful without removing rows

df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(
    lambda x: x.fillna(x.median())
)
```

## 6. Clean the column names
```python
# Make column names lowercase and replace spaces with underscores
# This makes the dataframe easier to work with in Python

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount_amount'})
```

## 7. Create an age-group feature
```python
# Create age groups using quartiles so the data is divided into four categories
# This is useful for grouping customers by life stage

labels = ['young adult', 'adult', 'middle age', 'senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels, duplicates='drop')
```

## 8. Convert purchase frequency into number of days
```python
# Map each purchase frequency category to an approximate number of days
# This helps turn categorical frequency into a numeric feature

frequency_mapping = {
    'fortnightly': 14,
    'weekly': 7,
    'monthly': 30,
    'quarterly': 90,
    'yearly': 365,
    'annually': 365,
    'every 3 months': 90,
    'bi-weekly': 14,
}

freq_col = 'frequency_of_purchases' if 'frequency_of_purchases' in df.columns else 'Frequency of Purchases'
df['purchase_frequency_days'] = (
    df[freq_col]
    .astype(str)
    .str.strip()
    .str.lower()
    .map(frequency_mapping)
)
```

## 9. Check the relationship between discount and promo code usage
```python
# Review whether discount applied and promo code used are identical columns
# This helps decide whether one of them is redundant

df[['discount_applied', 'promo_code_used']].head(10)
(df['discount_applied'] == df['promo_code_used']).all()
```

## 10. Remove the redundant column
```python
# Since both columns appear to represent the same thing, remove one of them

df = df.drop('promo_code_used', axis=1)
```

## Final reflection
This project helped me practice:
- loading and exploring a dataset
- cleaning messy column names
- handling missing values
- creating new features from existing data
- preparing data for future analysis or visualization
