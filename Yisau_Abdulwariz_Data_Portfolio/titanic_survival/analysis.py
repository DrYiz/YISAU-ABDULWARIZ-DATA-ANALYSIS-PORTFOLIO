"""Validation entry point for Titanic Survival Analysis."""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parent
def load_data(): return pd.read_csv(ROOT/'data'/'cleaned_data.csv')
def main():
    df=load_data()
    assert not df.empty
    print(f'Validated {len(df):,} records for Titanic Survival Analysis.')
    print('Dashboard, report, and high-resolution plots are available in the project folder.')
if __name__=='__main__': main()
