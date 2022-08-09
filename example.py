"""
This file contains examples of the intended use of this package.
"""
from visualization import *

# Example 1: (Main use) Obtaining DLI data and visualizing the data
# Convert raw data from http://pubdata.mlml.calstate.edu/mlml_last/weather/
# to PPFD and DLI, save data to .csv file, and graph DLI data.
dli_df = create_dli_df(1,1,2010,2,2,2011) # 01Jan2010 to 02Feb2011
dli_df.to_csv('dli_data.csv', index=True) # saves csv file to local directory
week_dli = weekly_dli(dli_df)
week_dli.to_csv('weekly_dli.csv', index=True)
month_dli = monthly_dli(dli_df)
month_dli.to_csv('monthly_dli.csv', index=True)
draw_figures(dli_df)


# Example 2: Retrieving raw data
# Retrieve and compile raw data
# from http://pubdata.mlml.calstate.edu/mlml_last/weather/
# and save data to .csv file
raw_data_df = Sun_expo().data_range(1,1,2010,2,2,2011) # 01Jan2010 to 02Feb2011
raw_data_df.to_csv('raw_data.csv', index=True)


# Example 3:Obtaining PAR data
# Convert raw data from http://pubdata.mlml.calstate.edu/mlml_last/weather/
# to PAR and save data to .csv file
par_df = create_df(1,1,2010,2,2,2011) # 01Jan2010 to 02Feb2011
par_df.to_csv('par_data.csv', index=True)
