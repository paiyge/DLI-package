"""
This module contains functions that create the graphs of DLI vs Date
"""

from calculate import *
from plotly.offline import plot
import plotly.express as px

def draw_scatterplot(dli_df, x='Date', y='DLI'):
    '''
    Draws a scatterplot of DLI vs Date by default.
    param ppdfd_df : pandas DataFrame : dataframe containing dates and DLI.
    param x : pandas Series, optional : data for the x-axis of the scatterplot, default is 'Date'.
    param y : pandas Series, optional : data for the y-axis of the scatterplot, default is 'DLI'.
    returns : none
    '''
    fig = px.scatter(dli_df, x, y)
    plot(fig, auto_open=True)


def draw_weekbar(dli_df):
    '''
    Draws a bar graph of DLI vs the week number
    param dli_df : pandas DataFrame : dataframe containing dates and DLI.
    returns : none
    '''
    week_df = weekly_dli(dli_df)
    week_df = week_df.reset_index()
    week_df['Year'] = week_df['Year'].astype(str)
    fig1 = px.bar(week_df, y='DLI', x='Week', color="Year", barmode='group')
    plot(fig1, auto_open=True)


def draw_monthbar(dli_df):
    '''
    Draws a bar graph of DLI vs month
    dli_df : pandas DataFrame : dataframe containing dates and DLI
    returns : none
    '''
    month_df = monthly_dli(dli_df)
    month_df = month_df.reset_index()
    month_df['Year'] = month_df['Year'].astype(str)
    fig2 = px.bar(month_df, y='DLI', x='Month', color="Year", barmode='group')
    plot(fig2, auto_open=True)

def draw_figures(dli_df):
    '''
    Draws a scatterplot of DLI vs Date, a bar graph of DLI vs the week number,
    and a bar graph of DLI vs month
    dli_df : pandas DataFrame : dataframe containing dates and DLI
    returns : none
    '''
    draw_scatterplot(dli_df)
    draw_weekbar(dli_df)
    draw_monthbar(dli_df)
