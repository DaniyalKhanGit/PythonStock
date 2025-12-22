 
import pandas as pd

df = pd.read_csv('prices.csv')

def parse_dataframe(df):
    required_columns = ['date', 'open', 'high', 'low', 'close', 'volume']

    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")
    
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    if df['date'].isna().any():
        raise ValueError("Invalid date format found in 'date' column.")

    numeric_cols = ['open', 'high', 'low', 'close', 'volume']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        if df[col].isna().any():
            raise ValueError(f"Non-numeric values found in '{col}' column.")

    if (df['high'] or df['low'] or df['close'] < 0).any():
        raise ValueError("Negative values found in numeric columns.")
    
    if (df['high'] < df['low']).any():
        raise ValueError("Inconsistent data: 'high' is less than 'low'.")
    
    if (df['volume'] < 0).any():
        raise ValueError("Negative values found in 'volume' column.")
    

    df = df.sort_values('date').reset_index(drop=True)

    if df['date'].duplicated().any():
        raise ValueError("Duplicate dates found in 'date' column.")
    
    if not df['date'].is_monotonic_increasing:
        raise ValueError("Dates are not in chronological order.")
    
    return df

parsed_df = parse_dataframe(df)


