
import pandas as pd
import numpy as np
import metrics 

# aim for something like {
# "trend": "Bullish",
#  "risk_level": "High",
#  "volatility_regime": "Elevated",
#  "max_drawdown": -0.184,
#  "flags": ["High volatility", "Recent drawdown"]
#}

def generate_insights(df):
    df = metrics.calculate_daily_returns(df)
    df = metrics.calculate_volatility(df)
    df = metrics.calculate_moving_average(df)

    max_dd = metrics.max_drawdown(df).max()
    avg_return = df['daily_return'].mean()

    def trend(df):
        if df['close'].iloc[-1] > df['moving_average'].iloc[-1]:
            trendf = "Bullish"
        else:
            trendf = "Bearish"

        return trendf

    def vol(df):
        vol = df['volatility'].iloc[-1]
        if vol < 0.01:
            vol_label = "Low"
        elif vol < 0.02:
            vol_label = "Normal"
        else:
            vol_label = "High"
        return vol_label
    
    max_dd = metrics.max_drawdown(df).min()

    def risk(df, max_dd):
        #vol risk
        if df['volatility'].iloc[-1] > 0.02:
            vol_risk = 1
        else:
            vol_risk = 0
        #drawdown risk
        max_dd = metrics.max_drawdown(df).min()

        if max_dd < -0.20:
            dd_risk = 1
        else:
            dd_risk = 0
        #trend risk
        latest = df.iloc[-1]
        if latest["close"] < latest["sma_50"]:
            trend_risk = 1
        else:
            trend_risk = 0
        #total risk
        total_risk = vol_risk + dd_risk + trend_risk
        
        if total_risk == 0:
            risk_level = "Low"
        elif total_risk == 1:
            risk_level = "Medium"
        else:
            risk_level = "High"
        return risk_level

        

    def flags(df):
        latest = df.iloc[-1]
        max_drawdown = metrics.max_drawdown(df).min()
        flags = []

        if latest['daily_return'] < -0.05:
            flags.append("Larger than (5%) daily drop")

        if latest['volatility_20'] > 0.02:
            flags.append("High constant volatility")

        if max_drawdown < -0.20:
            flags.append("Significant drawdown recently")

        if (
        latest["close"] < latest["sma_20"] and latest["sma_20"] < latest["sma_50"]
        ):
            flags.append("Bearish trend structure (price < SMA20 < SMA50)")
        
        recent_vol = df["volatility_20"].iloc[-5:].mean()
        long_vol = df["volatility_20"].mean()

        if recent_vol > 1.5 * long_vol:
            flags.append("Increasing volatility trend")

        return flags

    trend = trend(df)
    vol = vol(df)
    risk_level = risk(df)
    flags = flags(df)


    insights = {
        "trend": trend,
        "volatility": vol,
        "risk_level": risk_level,
        "max_drawdown": round(max_dd, 3),
        "average_return": round(avg_return, 4),
        "flags": flags
    }
    
    return insights



   

# Insights




