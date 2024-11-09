import pandas as pd

def clean_df(df):
    df.drop_duplicates(subset =["title", 'show_id'], inplace = True)
    df.dropna(subset = ["date_added"], inplace = True)
    df['date_added'] = df['date_added'].str.replace(',', '')
    df['date_added'] = pd.to_datetime(df['date_added'], format='%B %d %Y', errors='coerce', dayfirst=False)
    df['date_added'].fillna(method='ffill', inplace=True)  # Forward fill NaT values
    df['year_added'] = df['date_added'].dt.year
    df.sort_values(by = 'year_added', inplace = True)
    df.fillna(method='ffill', inplace=True)

    return df