#import tensorflow as tf
import numpy as np
import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup

def csv_to_df(csv):
    return(pd.read_csv(csv))


def clean_stats(df):
    df['GmID'] = 0
    df['WL'] = 0
    for x in range(len(df)):
        #Date
        date = df.loc[x, 'Date']
        date = list(date)
        newdate = ''
        for y in range(10):
            if date[y] != '-':
                newdate+=date[y]
        df.at[x, 'Date'] = float(newdate)

        #Age
        age = df.loc[x, 'Age']
        age = list(age)
        newage = ''
        for y in range(6):
            if age[y] != '-':
                newage+=age[y]
        df.at[x, 'Age'] = float(newage)

        #Location
        location = df.loc[x, 'Location']
        if location == '@':
            df.at[x, 'Location'] = 0
        else:
            df.at[x, 'Location'] = 1

        #GS
        gs = df.loc[x, 'GS']
        gs = list(gs)
        newgs = ''
        if len(gs) == 6:
            newgs = gs[-2]
        else:
            newgs = gs[-3] + gs[-2]
        newgs = float(newgs)
        if gs[0] == 'L':
            newgs = newgs * -1
        df.at[x, 'GS'] = newgs

        #Active
        if df.loc[x, 'Active'] == '0' or df.loc[x, 'Active'] == '1':
            df.at[x, 'Active'] = 1
        else:
            df.at[x, 'Active'] = 0

        #MP
        mp = df.loc[x, 'MP']
        mp = str(mp)
        mp = list(mp)
        newmp = ''
        for y in range(len(mp)):
            if mp[y] != ':':
                newmp+=mp[y]
        newmp = float(newmp)
        df.at[x, 'MP'] = newmp

        #GmID
        date = int(df.loc[x, 'Date'])
        tmID = df.loc[x, 'TmID']
        df.at[x, 'GmID'] = date + tmID

        #WL
        wl = df.loc[x, 'GS']
        if wl > 0:
            df.at[x, 'WL'] = 1
        else:
            df.at[x, 'WL'] = 0
    return df


def standerdize_stats(cleaned_df):
    df_means = cleaned_df.mean()
    df_stdevs = cleaned_df.std()
    normalized_df = cleaned_df
    columns = ['Age', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'GmSc', '+/-', 'TS%', 'eFG%', 'ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'ORtg', 'DRtg', 'BPM']
    for column in columns:
        normalized_df[column] = (normalized_df[column] - df_means[column])/df_stdevs[column]
    return normalized_df


def combine_team_stats(df):
    gameids = {}
    for x in range(len(df)):
        if df[x][-1] not in gameids:
            gameids[df[x][-1]] = []
        if df[x][8] == 1:
            gameids[df[x][-1]].append(df[x])
    return gameids



def rid_nans(df):
    df = df.fillna(0)
    return df


def to_numpy(df):
    data = df.to_numpy()
    return data

def save_df(df, title, path):
    df.to_csv(rf'{path}\{title}.csv', index=False)

def get_game_numbers(games):
    numbers = []
    for game in games:
        numbers.append(game)
    return numbers

def game_df(df, gameid):
    df = df[df['GmID'] == gameid]
    return df
