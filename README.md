# DS-5010-Project
Final package python project for DS 5010

DLI: https://en.wikipedia.org/wiki/Daily_light_integral 

1.	Title: Streamlining Daily Light Integral Calculations
2.	Authors: Paige Norris, Alan Cheung, Avinash Kasireddy, Marin Witherspoon
3.	Summary: The main purpose of this package is to take raw PAR data in micromoles and calculate the Daily Light Integral (DLI) in micromoles per m^2. DLI is the measurement of photosynthetically active photons that are delivered to a specific area over a 24-hour period. This value is useful for crop growth and determining which light intensities produce the best cultivation results. 
4.	Proposed design: 2-3 paragraphs describing in detail the modules, classes, and functions you will need to implement to provide the package’s intended functionality. Describe any external libraries you may need to use, and what aspects of the implementation will be your team’s work. 
  - This will be a 3 part package, each making up a module: data wrangling, calculations, visualization. 
   -  Data Wrangling: taking PAR data and making it pretty
    - Classes: User input dates as class object
    - Functions: scraping data from web source, user uploading data from local, formatting data sets into proper types
   - Calculations: Going from raw PAR data to DLI
    - Functions: Daily PAR total(micromol), PPFD(micromol/m^2 * sec), DLI(mol/m^2 * day)
   - Visualization: Use Plotly to make interactive graphs of DLI
    - Functions: one graph mapping it out
5. Potential challenges: Data wrangling from websites and the proper formatting of Date(times) I anticipate to be the most challenging. Most wetaher data bases I have seen do not have PAR recorded or if they do it is behind several 'clicks' (subpages I suppose) and/or needs a download. Unsure at the moment on how to come at and handle it. 

Questions for Professor:
1. Is this the proper use for classes and functions?
2. Is it proper to break up the modules by task? Or should they be separate classes within one module?
3. Is this enough work for the project?
