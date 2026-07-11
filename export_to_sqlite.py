import pandas as pd
import sqlite3

# Load the CSV file
csv_path = "customer_shopping_behavior.csv"
df = pd.read_csv(csv_path)

# Clean column names to be SQL-friendly
# Replace spaces with underscores and make lowercase

df.columns = df.columns.str.lower().str.replace(' ', '_')

# Rename the purchase amount column to a cleaner name
if 'purchase_amount_(usd)' in df.columns:
    df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount_amount'})

# Fill missing review ratings using the median rating for each category
if 'review_rating' in df.columns and 'category' in df.columns:
    df['review_rating'] = df.groupby('category')['review_rating'].transform(
        lambda x: x.fillna(x.median())
    )

# Create age groups using quartiles
labels = ['young adult', 'adult', 'middle age', 'senior']
if 'age' in df.columns:
    df['age_group'] = pd.qcut(df['age'], q=4, labels=labels, duplicates='drop')

# Map purchase frequency to approximate number of days
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

freq_col = 'frequency_of_purchases' if 'frequency_of_purchases' in df.columns else 'frequency_of_purchases'
if freq_col in df.columns:
    df['purchase_frequency_days'] = (
        df[freq_col]
        .astype(str)
        .str.strip()
        .str.lower()
        .map(frequency_mapping)
    )

# Remove the redundant promo code column if it exists
if 'promo_code_used' in df.columns:
    df = df.drop('promo_code_used', axis=1)

# Create a SQLite database file
sqlite_path = "customer_shopping_behavior.db"
conn = sqlite3.connect(sqlite_path)

# Write the cleaned dataframe to a table
# Replace 'customers' with the table name you want
df.to_sql('customers', conn, if_exists='replace', index=False)

# Commit and close
conn.commit()
conn.close()

print(f"Database created successfully: {sqlite_path}")
print("Table name: customers")
print("Columns exported:", df.columns.tolist())
