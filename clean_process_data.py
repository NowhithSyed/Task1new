import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# === 1. Load the Excel file ===
df_raw = pd.read_excel("marketing_campaign.xlsx", sheet_name="marketing_campaign", header=None)

# === 2. Split tab-separated data stored in a single column ===
df = df_raw[0].str.split('\t', expand=True)

# === 3. Use first row as header ===
df.columns = df.iloc[0]
df = df[1:].reset_index(drop=True)

# === 4. Clean column names ===
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("\t", "", regex=False)

# === 5. Remove duplicates ===
df.drop_duplicates(inplace=True)

# === 6. Handle missing or invalid income values ===
if 'income' in df.columns:
    df['income'] = pd.to_numeric(df['income'], errors='coerce')
    df['income'] = df['income'].fillna(df['income'].median())

# === 7. Convert columns to appropriate types ===
if 'year_birth' in df.columns:
    df['year_birth'] = pd.to_numeric(df['year_birth'], errors='coerce').astype('Int64')

if 'dt_customer' in df.columns:
    df['dt_customer'] = pd.to_datetime(df['dt_customer'], dayfirst=True, errors='coerce')

# === 8. Clean text fields ===
if 'marital_status' in df.columns:
    df['marital_status'] = df['marital_status'].str.strip().str.lower()

if 'education' in df.columns:
    df['education'] = df['education'].str.strip().str.title()

# === 9. Feature engineering: Age ===
if 'year_birth' in df.columns:
    df['age'] = 2025 - df['year_birth']

# === 10. (Optional) Normalize numeric features ===
# scaler = MinMaxScaler()
# numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
# df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# === 11. Save the cleaned dataset ===
output_file = "marketing_campaign_cleaned.csv"
df.to_csv(output_file, index=False)

print("✅ Data cleaned and saved to", output_file)
