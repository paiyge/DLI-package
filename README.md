# DS-5010-Project
Final package python project for DS 5010

### Purpose

Daily light integral (DLI) is the measurement of photosynthetically active photons delivered to a specific area over 24 hours. DLI is useful for crop growth and determining which light intensities produce the best cultivation results and is often utilized for indoor grows and hydroponics. The basis of DLI is photosynthetically active radiation (PAR), which is comprised of the photons with wavelengths between 400nm and 700nm, which organisms use for photosynthesis. To calculate DLI, raw PAR data is collected with a solar radiation probe, photosynthetic photon flux density (PPFD) is calculated using PAR, and is then converted to DLI by multiplying by a conversion factor and the light-hours. This package expedites the conversion of raw PAR data into refined DLI by enabling the user to scrape data directly from an online source and computes all calulations based soley on a user entered date range when using the package. 

DLI: https://en.wikipedia.org/wiki/Daily_light_integral

### Organization

- \_\_init\_\_.py : Initialization script
- scrapy_updatedNames.py : scrapes PAR data from site and formats 
- calculate.py : computes subcalculations to go from raw PAR to DLI
- visualization.py: creates plots of DLI by day, week, and month
- test.py : tests scrapy_updatedNames.py, calculate.py, and visualization.py
- example.py : example code of intended use of the package

### External Libraries/Packages
The following libaries/packages are required and need to installed for this package to function.
- Numpy
- Pandas
- Pipe
- Plotly

### Usage Examples
- Examples are from example.py 

```
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
```
