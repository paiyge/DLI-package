import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

#Checks / corrects entered day values
def check_day(day):
    try:
        if day>31 or day<1:
            print("day input not valid")
        elif len(str(day))==1:
            day='0'+str(day)
        else:
            pass
        return str(day)
    except:
        print("day input not valid")
 
#Checks / corrects entered month value
def check_month(month):
    try:
        if month >12 or month<1:
            print("input not valid")
        elif len(str(month)) ==1:
            month='0'+str(month)
        else:
            pass
        return str(month)

    except:
        print("month input not valid")
    
#Checks / corrects entered year value
current_year=int(datetime.date.today().strftime("%Y"))
def check_year(year):
    try:
        if len(str(year))==2:
            if int(year)>int(str(current_year)[-2:]):
                year='19'+str(year)
            else:
                year='20'+str(year)
        elif int(year)>current_year or int(y)<int(2000):
            print("data only available from "+str(2000)+" to "+str(current_year))
        else:
            pass
        return str(year)
    except:
        print("year input not valid")

"""
#user enters date range

from_date=input("From: mm/dd/yyyy: ").split("/")
from_m=int(from_date[0])
from_d=int(from_date[1])
from_y=int(from_date[2])

check_day(from_d)
check_month(from_m)
check_year(from_y)

to_date=input("To: mm/dd/yyyy: ").split("/")
to_m=int(to_date[0])
to_d=int(to_date[1])
to_y=int(to_date[2])

check_day(to_d)
check_month(to_m)
check_year(to_y)

"""
#Testing block
from_d=int(4)
from_m=int(5)
from_y=int(2010)

to_d=int(17)
to_m=int(10)
to_y=int(2010)
#

#standardizes data time format
from_date=datetime.datetime(from_y,from_m,from_d)
to_date=datetime.datetime(to_y,to_m,to_d)
def date_strip(x):
    return datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

dfs=[]
print("compiling in process, please wait a moment.")
#Iterates through links and converts to pandas data frame.
while from_date<=to_date:
    #iterate count up by month
    from_date += relativedelta(months=1)
    y=str(date_strip(str(from_date)).year)
    m=str(date_strip(str(from_date)).month-1)
    year=check_year(int(y))
    month=check_month(int(m))
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
df['psto_time']=pd.to_datetime(df['psto_time'])
#filters data frame by day
df[(df['pst_time']>=from_date)&(df['pst_time']<=to_date)]

print("Done!:")
print(df)
