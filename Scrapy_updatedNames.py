import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

class Sun_expo:

    def data_range(self, from_m:int, from_d:int, from_y:int, to_m:int, to_d:int, to_y:int):

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
            while from_date<=to_date:
                #iterate count up by month
                from_date += relativedelta(months=1)
                year=from_date.strftime("%Y")
                month=datetime.date(day=1,month=from_date.month-1,year=from_date.year).strftime("%m")
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
            df=df[(df['pst_time']>=from_date)&(df['pst_time']<=to_date+relativedelta(days=1))]

            print("Done!")
            
            pd.DataFrame(df).sort_values(by="pst_time")
            print(df['pst_time'].iloc[0])
            print(df['pst_time'].iloc[-1])
            return print(df)
