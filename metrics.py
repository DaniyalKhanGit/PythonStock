
import pandas as pd
import numpy as np


def calculate_daily_returns(df):
        for row in df.itertuples():
            if row.Index == 0:
                df.at[row.Index, 'daily_return'] = 0.0
            else:
                pclose = df.at[row.Index - 1, 'close']
                close = df.at[row.Index, 'close']
                daily_return = (close - pclose) / pclose
                df.at[row.Index, 'daily_return'] = daily_return
        return df

def calculate_volatility(df, window=20):
    df[f'volatility_{window}'] = df['daily_return'].rolling(window=window).std() * np.sqrt(252)
    
    return df

def calculate_moving_average(df, windows=[20, 50]):
    for w in windows:
        df[f'sma_{w}'] = df['close'].rolling(window=w).mean()
    return df

def max_drawdown(df):
    for row in df.itertuples():
        if row.Index == 0:
            df.at[row.Index, 'max_drawdown'] = 0.0
        else:
            df.at[row.Index, 'max_drawdown'] = (df.at[row.Index, 'high'] - df.at[row.Index, 'low']) / df.at[row.Index, 'high']

    df['max_drawdown'] = df['max_drawdown'].astype(float)
    return df
    
def calculate_daily_returns(df):
        for row in df.itertuples():
            if row.Index == 0:
                df.at[row.Index, 'daily_return'] = 0.0
            else:
                pclose = df.at[row.Index - 1, 'close']
                close = df.at[row.Index, 'close']
                daily_return = (close - pclose) / pclose
                df.at[row.Index, 'daily_return'] = daily_return
        return df



def calculate_metrics(df):
    
    df = calculate_daily_returns(df)
    df = calculate_volatility(df)
    df = calculate_moving_average(df)
    df = max_drawdown(df)
    
    return df

