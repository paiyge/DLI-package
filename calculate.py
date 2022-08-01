import pandas as pd

import scrape
import pipe

def create_df():
    '''

    :return: par_df
    '''
    df = scrape.df

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
    #ppfd = df.groupby(['Date'])['PAR'].mean()
    #ppfd_df = pd.DataFrame("")
    ppfd_df = pd.DataFrame(df.groupby(['Date'])['PAR'].mean())
    #pd.DataFrame({"Date": df.groupby(by="Date")})
    print(ppfd_df)
    return  calculate_dli(ppfd_df)

def calculate_dli(ppfd_df):
    # Mutiply ppfd * 0.0036 * 24 #0.0864
    ppfd_df['DLI'] = ppfd_df['PAR'] * 0.0036 * 24
    print(ppfd_df)
    return ppfd_df


if __name__ == "__main__":
    calculate_ppfd(create_df())