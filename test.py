from Scrapy_updatedNames import Sun_expo
from calculate import *
from visualization import *
import numpy
import pytest
s = Sun_expo()

def test_data_range():
    # EXAMPLE 1:
    # correct usage: can process over numerous months and years.
    # Returns: a pandas data frame in the terminal.
    print(s.data_range(11,10,2010,2,17,2011))

    # EXAMPLE 2:
    # incorrect usage: The user has entered a string where they need an integer.
    # Returns: The Datetime package will return ValueError, telling the user to enter an integer.
    pytest.raises(TypeError,s.data_range,"June",5,2010,10,17,2010)

    # EXAMPLE 3:
    # tollerable usage: The user has ented a 2 digit year.
    # Returns: The Datetime package will autocorrect this to 2010 and will still sucessfully return data.
    print(s.data_range(4,5,10,10,17,10))

    # EXAMPLE 4:
    # incorrect ussage: The user had ented a day outside the usual 31 days
    # of the month.
    # Returns: The datetime package will inform the user that the entered value is outside range.
    pytest.raises(ValueError,s.data_range,4,50,2010,10,17,2010)

    # EXAMPLE 5:
    # incorrect ussage: The user forgot to enter a value.
    # Returns: error missing value.
    pytest.raises(TypeError,s.data_range,5,2010,10,17,2010)

    # EXAMPLE 6:
    # correct usage: Here the user is calling data that is not available.
    # Returns: request the user enter dates from 11/2000 forward.
    print(s.data_range(5,15,1910,10,17,1920))

def test_create_df():
    # data frame should contain only date and PAR data from 10Nov2010 to
    # 17Feb2011
    print(create_df(4,5,2010,2,17,2011))

def test_calculate_ppfd():
    df1 = pd.DataFrame(data={'DateTime':[2011-4-5, 2011-4-5], 'PAR':[10, 20]})
    print(calculate_ppfd(df1))


if __name__ == '__main__':
    test_data_range()
    # test_create_df()
    # test_calculate_ppfd()
