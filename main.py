from helperFunctions import *
if __name__ == '__main__':\
    #Scraping league stats from 2010
    save_df(leagueScraper('2010'), 'League2010', r"#Input computer path here#")
    csv = r"#path to new csv"
    df = csv_to_df(csv)
    cleaneddf = clean_stats(df)
    save_df(cleaneddf, 'League2010cleaned', r"#Input computer path here#")
    standerdized_df = standerdize_stats(cleaneddf)
    save_df(standerdized_df, 'League2010standerdized', r"#Input computer path here#")