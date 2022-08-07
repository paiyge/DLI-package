'''
This module contains functions that generate data frames with PAR, PPFD,
and/or DLI data.
'''

import pandas as pd
from Scrapy_updatedNames import *
import pipe

def create_df(from_m:int, from_d:int, from_y:int, to_m:int, to_d:int, to_y:int):
    '''
    Creates data frame containing only dates and PAR values
    param from_m:int: beginning month as int
    param from_d:int: beginning day as int
    param from_y:int: beginning year as int
    param to_m:int: ending month as int
    param to_d:int: ending day as int
    param to_y:int: ending year as int
    return par_df: dataframe containing dates and PAR
    '''
    data = Sun_expo()
    df = data.data_range(from_m, from_d, from_y, to_m, to_d, to_y)
    par_df = df[['pst_time', 'sr_1']].copy()
    par_df = par_df.dropna()
    par_df = par_df.rename(columns={'pst_time': 'DateTime', 'sr_1': 'PAR'})

    par_df.loc[par_df['PAR'] < 0, 'PAR'] = 0  # PAR cannot be < 0

    return par_df


def calculate_ppfd(par_df):
    '''
    Calculates PPFD by finding mean of PAR values taken per each day
    param par_df: dataframe containing PAR values collected by day
    return ppfd_df: dataframe containing dates, PAR, and PPFD
    '''
    df = par_df.copy()
    df['Date'] = pd.to_datetime(df['DateTime']).dt.date

    #convert date to unix time to be able average the data
    df['UnixTime'] = pd.to_datetime(df['DateTime']).astype(int) / 10**9

    #create one data frame by merging date/time and PAR
    ppfd_df = pd.DataFrame(df.groupby(['Date'])['UnixTime'].mean())
    ppfd_df['Date'] = pd.to_datetime(ppfd_df['UnixTime'], unit='s')
    ppfd = pd.DataFrame(df.groupby(['Date'])['PAR'].mean())
    ppfd.rename(columns = {'PAR':'PPFD'}, inplace = True)
    ppfd_df = ppfd_df.join(ppfd)

    return  ppfd_df


def calculate_dli(ppfd_df):
    '''
    Calculates DLI from PPFD, the integral duration, and a conversion factor
    param ppfd_df: dataframe containing dates, PAR, and PPFD
    return: dataframe with DLI appended
    '''
    # DLI = ppfd * 0.0036 * 24 #0.0864
    ppfd_df['DLI'] = ppfd_df['PPFD'] * 0.0036 * 24

    return ppfd_df


def create_dli_df(from_m:int, from_d:int, from_y:int, to_m:int, to_d:int, to_y:int):
    '''
    Creates data frame from Sun_expo class
    param from_m:int: beginning month as int
    param from_d:int: beginning day as int
    param from_y:int: beginning year as int
    param to_m:int: ending month as int
    param to_d:int: ending day as int
    param to_y:int: ending year as int
    return par_df: dataframe containing dates, PAR, PPFD, and DLI
    '''
    par_df = create_df(from_m, from_d, from_y, to_m, to_d, to_y)
    ppfd_df = calculate_ppfd(par_df)
    dli_df = calculate_dli(ppfd_df)

    return dli_df


def weekly_dli(dli_df):
    '''
    Creates a data frame with the week number and the year as indices and
    the week's average DLI as a column

    Parameters
    ----------
    dli_df : pandas DataFrame
        Data frame containing dates and DLI. Date is in unix time.

    Returns
    -------
    week_df : pandas DataFrame
        Data frame with the week number the year, and the week's average DLI

    '''
    dli_df = dli_df.copy()
    dli_df['Week'] = (pd.to_datetime
                       (dli_df['UnixTime'], unit='s').dt.isocalendar().week)
    dli_df['Year'] = (pd.to_datetime
                       (dli_df['UnixTime'], unit='s').dt.year)
    week_df = pd.DataFrame(dli_df.groupby(['Year','Week'])['DLI'].mean())

    return week_df


def monthly_dli(dli_df):
    '''
    Creates a data frame with the month number and the year as indices and
    the month's average DLI as a column

    Parameters
    ----------
    dli_df : pandas DataFrame
        Data frame containing dates and DLI. Date is in unix time.

    Returns
    -------
    month_df : pandas DataFrame
        Data frame with the month number and the year as indices and
        the month's average DLI as a column

    '''
    dli_df = dli_df.copy()
    dli_df['Month'] = (pd.to_datetime
                       (dli_df['UnixTime'], unit='s').dt.month)
    dli_df['Year'] = (pd.to_datetime
                       (dli_df['UnixTime'], unit='s').dt.year)
    month_df = pd.DataFrame(dli_df.groupby(['Year','Month'])['DLI'].mean())

    return month_df



if __name__ == "__main__":
    # par_df = create_df(4,5,2010,10,17,2010)
    # print(par_df)
    # ppfd_df = calculate_ppfd(par_df)
    # ppfd_df.to_csv('data2.csv', index=True)
    # print(ppfd_df)
    # dli_df = calculate_dli(ppfd_df)
    dli_df1 = create_dli_df(4,5,2010,10,17,2010)
