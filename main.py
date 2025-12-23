
import pandas as pd
import numpy as np
from metrics import calculate_metrics
from insights import generate_insights
from parser import parse_dataframe
from cli import parse_args


# example data input
# date,open,high,low,close,volume
# 2024-12-01,172.4,175.1,170.8,174.9,84230000

def main():
    df = pd.read_csv(parse_args('prices.csv'))
    parsed_df = parse_dataframe(df)
    insights = generate_insights(calculate_metrics(parsed_df))
    print(insights)


    
if __name__ == "__main__":
    main()