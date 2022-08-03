import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

class Sun_expo:
    """
    Pulls data from online source and usses that data to estimate sun exposure.
    """

    def data_range(self, from_m:int, from_d:int, from_y:int, to_m:int, to_d:int, to_y:int):
        """
        Pulls data off online csv files based on entered dates.
        Parameters
        ----------
        from_m : int
            The oldest month to pull.
        from_d : int
            The oldest day to pull.
        from_y : int
            The oldest month to pull.
        to_m : int
            The newest month to pull.
        to_d : int
            The newest day to pull.
        to_y : int
            The newest year to pull.

        Returns
        -------
        df : Pandas dataframe
            A dataframe contining data only from within the entered dates.

        """

        #standardizes data time format
        from_date=datetime.date(from_y,from_m,from_d)
        to_date=datetime.date(to_y,to_m,to_d)
        
        oldest_data=datetime.date(2000,11,1)
        if from_date < oldest_data or to_date > datetime.date.today():
            print("data is only available from ", oldest_data," to present.")
        else:
            dfs=[]
            print("compiling data between",from_date,"-",to_date,"please wait a moment.")
            #Iterates through links and converts to pandas data frame.
            first_date=from_date-relativedelta(months=1)
            while first_date<to_date-relativedelta(months=1):
                #iterate count up by month
                first_date += relativedelta(months=1)
                year=first_date.strftime("%Y")
                month=first_date.strftime("%m")
                try:
                    dfs.append(pd.read_csv('http://pubdata.mlml.calstate.edu/mlml_last/weather/'+year+"-"+month+".csv"))
                except: #if data is missing pass
                    pass

            #compiles all pulled csv files
            df = pd.concat(dfs, ignore_index=True)
            #converts column to datetime
            df['pst_time']=pd.to_datetime(df['pst_time'])
            #filters data frame by day
            df[(df['pst_time']>=pd.to_datetime(from_date))&(df['pst_time']<=pd.to_datetime(to_date))]

            print("Done!")
            return df