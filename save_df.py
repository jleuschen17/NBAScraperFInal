def save_df(df, title, path):
    df.to_csv(rf'{path}{title}.csv', index=False)