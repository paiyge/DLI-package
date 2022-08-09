# TO DO

- calculate DLI
- create a visulation .rmd
- create a main file for execution
- make readme for repo
- write the project report
- convert scrapy to class

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
The following libaries/packages are used in this package. They need to be installed for this package to work properly.
-Numpy
-Pandas
-Pipe
-Plotly


### Usage Examples
- Examples are from example.py 
