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
        from_date=datetime.datetime(from_y,from_m,from_d)
        to_date=datetime.datetime(to_y,to_m,to_d)

        dfs=[]
        print("compiling in process, please wait a moment.")
        #Iterates through links and converts to pandas data frame.
        while from_date<=to_date:
            #iterate count up by month
            from_date += relativedelta(months=1)
            y=str(datetime.datetime.strptime(str(from_date), '%Y-%m-%d %H:%M:%S').year)
            m=str(datetime.datetime.strptime(str(from_date), '%Y-%m-%d %H:%M:%S').month-1)
            year=str(y)
            month=str(m)
            try:
                dfs.append(pd.read_csv('http://pubdata.mlml.calstate.edu/mlml_last/weather/'+year+"-"+month+".csv"))
            except: #if data is missing pass
                pass
        #converts from_date and to_time back to original.    
        from_date=datetime.datetime(from_y,from_m,from_d)
        to_date=datetime.datetime(to_y,to_m,to_d)

        #compiles all pulled csv files
        df = pd.concat(dfs, ignore_index=True)
        #converts column to datetime
        df['pst_time']=pd.to_datetime(df['pst_time'])
        #filters data frame by day
        df[(df['pst_time']>=from_date)&(df['pst_time']<=to_date)]

        print("Done!")
        return df

        
if __name__ == "__main__":
    s=Sun_expo()
    s.data_range(4,5,2010,10,17,2010)
