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

    par_df.loc[par_df['PAR'] < 0, 'PAR'] = 0

    return par_df


def calculate_ppfd(par_df):
    '''
    Calculates PPFD by finding mean of PAR values taken per each day
    param par_df: dataframe containing PAR values collected by day
    return ppfd_df: dataframe containing dates, PAR, and PPFD
    '''
    df = par_df.copy()
    df['Date'] = pd.to_datetime(df['DateTime']).dt.date

    #convert date to unix time to average the data
    df['UnixTime'] = pd.to_datetime(df['DateTime']).astype(int) / 10**9

    #create one dataframe by merging date/time and PAR
    ppfd_df = pd.DataFrame(df.groupby(['Date'])['UnixTime'].mean())
    ppfd_df['Date'] = pd.to_datetime(ppfd_df['UnixTime'], unit='s')
    par = pd.DataFrame(df.groupby(['Date'])['PAR'].mean())

    ppfd_df = ppfd_df.join(par)
    return  calculate_dli(ppfd_df)


def calculate_dli(ppfd_df):
    '''
    Calculates DLI from PPFD, the integral duration, and a conversion factor
    param ppfd_df: dataframe containing dates, PAR, and PPFD
    return: dataframe containing dates, PAR, PPFD, and DLI
    '''
    # Mutiply ppfd * 0.0036 * 24 #0.0864
    ppfd_df['DLI'] = ppfd_df['PAR'] * 0.0036 * 24
    
    return ppfd_df


if __name__ == "__main__":
    par_df = create_df(4,5,2010,10,17,2010)
    # print(par_df)
    ppfd_df = calculate_ppfd(par_df)
    # ppfd_df.to_csv('data2.csv', index=True)
    # print(ppfd_df)
