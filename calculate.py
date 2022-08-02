import pandas as pd
from Scrapy_updatedNames import *
import pipe

def create_df(from_m:int, from_d:int, from_y:int, to_m:int, to_d:int, to_y:int):
    '''

    :return: par_df
    '''
    data = Sun_expo()
    df = data.data_range(from_m, from_d, from_y, to_m, to_d, to_y)
    par_df = df[['pst_time', 'sr_1']].copy()
    par_df = par_df.dropna()
    par_df = par_df.rename(columns={'pst_time': 'DateTime', 'sr_1': 'PAR'})
    return par_df


def calculate_ppfd(par_df):
    '''
    :return:ppfd_df
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
    # Mutiply ppfd * 0.0036 * 24 #0.0864
    ppfd_df['DLI'] = ppfd_df['PAR'] * 0.0036 * 24
    # print(ppfd_df)
    return ppfd_df


if __name__ == "__main__":
    par_df = create_df(4,5,2010,10,17,2010)
    # print(par_df)
    ppfd_df = calculate_ppfd(par_df)
    # ppfd_df.to_csv('data2.csv', index=True)
    # print(ppfd_df)
