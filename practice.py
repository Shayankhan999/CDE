import pandas as pd
import numpy as np

print("--- Step 1: Data Load Ho Raha Hy ---")
df = pd.read_csv('supermarket_sales_case_study.csv')


rows_initial, cols_initial = df.shape
print(f"Shuru mein Rows: {rows_initial}, Columns: {cols_initial}\n")


print("--- Step 2: Data Ka Audit ---")
print("Missing values har column mein:\n", df.isnull().sum())
print("\nExact duplicate rows ki tadad:", df.duplicated().sum())
print("Duplicate Invoice IDs ki tadad:", df.duplicated(subset=['Invoice ID']).sum())
print("Gender columns ki unique values:", df['Gender'].unique())
print("Payment columns ki unique values:", df['Payment'].unique())


print("--- Step 3: Exact Duplicate Rows Ko Delete Karna ---")

df = df.drop_duplicates()

print("Rows bache:", len(df))


print("--- Step 4: Duplicate Invoice IDs Theek Karna ---")


df = df.drop_duplicates(subset=['Invoice ID'], keep='last')

print("Rows bache:", len(df))


print("--- Step 5: Text Columns Ko Standardise Karna ---")

df['Gender'] = df['Gender'].astype(str).str.strip().str.lower()
df['Payment'] = df['Payment'].astype(str).str.strip().str.lower()

# Sahi spellings par map karna
gender_map = {'male': 'Male', 'female': 'Female'}
payment_map = {'cash': 'Cash', 'credit card': 'Credit card', 'ewallet': 'Ewallet'}

df['Gender'] = df['Gender'].map(gender_map)
df['Payment'] = df['Payment'].map(payment_map)
print("Text cleaning mukammal!\n")


print("--- Step 6: Negative Quantities Ko Positive Karna ---")
df['Quantity'] = df['Quantity'].abs()
print("Quantities theek ho gayin!\n")


print("--- Step 7: Mixed Dates Ko Format Karna ---")

date_format_1 = pd.to_datetime(df['Date'], format='%m/%d/%Y', errors='coerce')
date_format_2 = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')

df['Clean_Date'] = date_format_1.fillna(date_format_2)
print("Dates parse ho gayin!\n")


print("--- Step 8: Total Calculations Check Karna ---")
calculated_total = df['Quantity'] * df['Unit price'] * 1.05

difference = (df['Total'] - calculated_total).abs()
df['Total'] = np.where(difference > 0.50, calculated_total, df['Total'])
print("Totals verify aur correct ho gaye!\n")

# ==========================================
# Audit Trail Dictionary Initialization (Yahan add karein)
# ==========================================
audit_trail = {}
audit_trail["Shuru (Initial)"] = len(df)

print("--- Step 9: Bache Hue Missing Data Ko Handle Karna ---")
df['Customer type'] = df['Customer type'].fillna('Unknown')

median_rating = df['Rating'].median()
df['Rating'] = df['Rating'].fillna(median_rating)

df = df.dropna(subset=['Clean_Date'])
audit_trail["After Step 9 (Clean Missing)"] = len(df)
print(f"Final Rows bache: {len(df)}\n")


print("--- Step 10: Complete Audit Trail Summary ---")
for step, count in audit_trail.items():
    print(f"{step} -> Rows Mojood Hain: {count}")
print("-" * 50 + "\n")



# SECTION 2: ANSWERING THE BRIEF


print("--- Brief Sawal 1: Adding Time Columns ---")
df['Year'] = df['Clean_Date'].dt.year
df['Quarter'] = df['Clean_Date'].dt.to_period('Q').astype(str)
df['Day_of_week'] = df['Clean_Date'].dt.day_name()
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour
print("Time columns successfully add ho gaye hain!\n")

print("--- Brief Sawal 2: Bucket the Trading Day ---")
# Hour ke mutabiq trading shifts banana
def assign_bucket(hour):
    if 10 <= hour < 13: return 'Morning 10-13'
    elif 13 <= hour < 17: return 'Afternoon 13-17'
    elif 17 <= hour <= 21: return 'Evening 17-21'
    return 'Closed'

df['Day_Bucket'] = df['Hour'].apply(assign_bucket)

# Transactions Per Hour calculate karna matching the formula
bucket_counts = df['Day_Bucket'].value_counts()
hours_mapper = {'Morning 10-13': 3, 'Afternoon 13-17': 4, 'Evening 17-21': 4}

print("Transactions per hour down the shifts:")
for bucket, hours in hours_mapper.items():
    tx_count = bucket_counts.get(bucket, 0)
    tx_per_hour = tx_count / hours
    print(f" * {bucket}: {tx_per_hour:.2f} transactions/hour")
print("\n")

print("--- Brief Sawal 3 & 4: Compare Against Target & Summary ---")
# Branch aur Quarter ke mutabiq revenue nikalna
branch_summary = df.groupby(['Branch', 'Quarter'])['Total'].sum().reset_index()
branch_summary.rename(columns={'Total': 'Revenue'}, inplace=True)

# Target column add karna ($100,000 per branch)
branch_summary['Target'] = 100000
branch_summary['Variance'] = branch_summary['Revenue'] - branch_summary['Target']
branch_summary['% of Target'] = (branch_summary['Revenue'] / branch_summary['Target']) * 100
branch_summary['Hit'] = branch_summary['Revenue'] >= branch_summary['Target']

print(branch_summary[['Branch', 'Quarter', 'Revenue', 'Variance', '% of Target', 'Hit']])
print("\n")

# ==========================================
# Clean Data Export
# ==========================================
df.to_csv('cleaned_supermarket_sales.csv', index=False)
print("🎉 Cleaned data 'cleaned_supermarket_sales.csv' ke naam se save ho gaya hy!")