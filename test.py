exec(open('./Scrapy_updatedNames.py').read())
s=Sun_expo()

#EXAMPLE 1:
#correct usage: can process over numerous months and years.
#Returns: a pandas data frame in the terminal.
print(s.data_range(11,10,2010,2,17,2011))

#EXAMPLE 2:
#incorrect usage: The user has entered a string where they need an integer.
#Returns: The Datetime package will return an error, telling the user to enter an integer.
s.data_range("June",5,2010,10,17,2010)

#EXAMPLE 3:
#tollerable usage: The user has ented a 2 digit year.
#Returns: The Datetime package will autocorrect this to 2010 and will still sucessfully return data.
print(s.data_range(4,5,10,10,17,10))

#EXAMPLE 4:
#incorrect ussage: The user had ented a day outside the usual 31 days
#of the month.
#Returns: The datetime package will inform the user that the entered value is outside range.
s.data_range(4,50,2010,10,17,2010)

#EXAMPLE 5:
#incorrect ussage: The user forgot to enter a value.
#Returns: error missing value.
s.data_range(5,2010,10,17,2010)

#EXAPME 6:
#correct usage: Here the user is calling data that is not available.
#Returns: request the user enter dates from 11/2000 forward.
s.data_range(5,1910,10,17,1920)
