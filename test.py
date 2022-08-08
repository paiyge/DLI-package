'''
This file contains the unit tests for this package.
'''
from Scrapy_updatedNames import Sun_expo
from calculate import *
from visualization import *
import pytest
s = Sun_expo()

def test_data_range():
    '''
    tests the data_range() method of the Sun_expo class in
    Scrapy_updatedNames.py
    '''

    # Expected: data frame
    print(s.data_range(11,10,2010,2,17,2011))

    # Expected: ValueError, telling the user to enter an integer.
    # Since the user has entered a string where they need an integer.
    pytest.raises(TypeError,s.data_range,"June",5,2010,10,17,2010)

    # Expected: ValueError
    # Since the user has ented a 2 digit year.
    print(s.data_range(4,5,10,10,17,10))

    # Expected: ValueError
    # Since the user had ented a day outside the usual 31 days of the month.
    pytest.raises(ValueError,s.data_range,4,50,2010,10,17,2010)

    # Expected: ValueError
    # Since the user forgot to enter a value.
    pytest.raises(TypeError,s.data_range,5,2010,10,17,2010)

    # Expected: Request the user enter dates from 11/2000 forward.
    # Since the user is calling data that is not available.
    print(s.data_range(5,15,1910,10,17,1920))


def test_create_df():
    '''
    tests the create_df() function in calculate.py
    '''
    # data frame should contain only date and PAR data from 10Nov2010 to
    # 17Feb2011
    print(create_df(4,5,2010,2,17,2011))


def test_calculate_ppfd():
    '''
    tests the calculate_ppfd() function in calculate.py
    '''
    # Expected: one row with PPFD=15 and Date incorrect
    # since date is in wrong format
    df1 = pd.DataFrame(data={'DateTime':[2010-1-24, 2012-1-25], 'PAR':[10, 20]})
    print(calculate_ppfd(df1))

    # Expected: Two rows with correct Dates and PPFD = 20 & 30
    df2 = pd.DataFrame(data={'DateTime':[pd.Timestamp('2010-01-24 23:55:01'),
                                         pd.Timestamp('2010-01-25 23:56:01')],
                             'PAR':[20,30]})
    print(calculate_ppfd(df2))

    # Expected: One row with correct Dates and PPFD = 25
    df3 = pd.DataFrame(data={'DateTime':[pd.Timestamp('2010-01-24 23:55:01'),
                                         pd.Timestamp('2010-01-24 23:56:01')],
                             'PAR':[20,30]})
    print(calculate_ppfd(df3))

    # Expected: KeyError since column name is 'Date' instead of 'DateTime'
    df4 = pd.DataFrame(data={'Date':[pd.Timestamp('2010-01-24 23:55:01'),
                                         pd.Timestamp('2010-01-24 23:56:01')],
                             'PAR':[20,30]})
    pytest.raises(KeyError, calculate_ppfd, df4)


def test_calculate_dli():
    '''
    tests the calculate_dli() function in calculate.py
    '''
    # Expected: data frame with PPFD and DLI= 0, 0.0864, 0.1728
    df1 = pd.DataFrame(data={"PPFD":[0,1,2]})
    print(calculate_dli(df1))

    # Expected KeyError since column name is not'PPFD'
    df2 = pd.DataFrame(data={'ppfd':[0,1,2]})
    pytest.raises(KeyError, calculate_dli, df2)


def test_create_dli_df():
    '''
    tests the create_dli_df() function in calculate.py
    '''
    # Expected: data frame with Date as index
    # and UnixTime, Date, PPFD, and DLI as columns from 05Apr2010 to 17Feb2011
    print(create_dli_df(4,5,2010,2,17,2011))


def test_weekly_dli():
    '''
    tests the weekly_dli() function in calculate.py
    '''
    # Expected: ValueError
    # since the inputted UNIX time is in milliseconds, instead of seconds
    df1 = pd.DataFrame(data={'UnixTime':[1659412800000, 1659499200000],
                            'DLI':[0,1]})
    pytest.raises(ValueError, weekly_dli, df1)

    # Expected: one row with Week=31 and DLI=0.5
    # Dates inputted are 02Aug2022 and 03Aug2022 in UNIX time in seconds
    df2 = pd.DataFrame(data={'UnixTime':[1659412800, 1659499200],
                            'DLI':[0,1]})
    print(weekly_dli(df2))

    # Expected: KeyError since column name should be 'UnixTime', not 'Time'
    df3 = pd.DataFrame(data={'Time':[1659412800, 1659499200],
                            'DLI':[0,1]})
    pytest.raises(KeyError, weekly_dli, df3)


def test_monthly_dli():
    '''
    tests the monthly_dli() function in calculate.py
    '''
    # Expected: ValueError
    # since the inputted UNIX time is in milliseconds, instead of seconds
    df1 = pd.DataFrame(data={'UnixTime':[1659412800000, 1659499200000],
                            'DLI':[0,1]})
    pytest.raises(ValueError, monthly_dli, df1)

    # Expected: one row with Month=8 and DLI=0.5
    # Dates inputted are 02Aug2022 and 03Aug2022 in UNIX time in seconds
    df2 = pd.DataFrame(data={'UnixTime':[1659412800, 1659499200],
                            'DLI':[0,1]})
    print(monthly_dli(df2))

    # Expected: KeyError since column name should be 'UnixTime', not 'Time'
    df3 = pd.DataFrame(data={'Time':[1659412800, 1659499200],
                            'DLI':[0,1]})
    pytest.raises(KeyError, monthly_dli, df3)


def test_draw_scatterplot():
    '''
    tests the draw_scatterplot() function in visualization.py
    '''
    # Expected: ValueError since arguments were not specified and
    # default arguments (x='Date', y='DLI') were columns od df1
    df1 = pd.DataFrame(data={'a':[0,1,2], 'b':[4,5,6]})
    pytest.raises(ValueError, draw_scatterplot, df1)

    # Expected: creates a scatterplot in default web browser with
    # 'a' as x-axis and 'b' as y-axis
    df2 = pd.DataFrame(data={'a':[0,1,2], 'b':[4,5,6]})
    draw_scatterplot(df2, 'a', 'b')

    # Expected: creates a scatterplot in default web browser with
    # 'Date' as x-axis and 'DLI' as y-axis
    df2 = pd.DataFrame(data={'Date':[0,1,2], 'DLI':[4,5,6]})
    draw_scatterplot(df2)



if __name__ == '__main__':
    # test_data_range()
    # test_create_df()
    # test_calculate_ppfd()
    # test_calculate_dli()
    # test_create_dli_df()
    # test_weekly_dli()
    # test_monthly_dli()
    test_draw_scatterplot()
