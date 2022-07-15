import pandas as pd
import datetime
import numpy as np
from dateutil.relativedelta import relativedelta

#try on pc
#remove export to csv
#work on pathname

#Checks / corrects entered day values
def check_day(d):
    try:
        if d>31 or d<1:
            print("day input not valid")
        elif len(str(d))==1:
            d='0'+str(d)
        else:
            pass
        return str(m)
    except:
        print("day input not valid")
 
#Checks / corrects entered month value
def check_month(m):
    try:
        if m >12 or m<1:
            print("input not valid")
        elif len(str(m)) ==1:
            m='0'+str(m)
        else:
            pass
        return str(m)

    except:
        print("month input not valid")
    
#Checks / corrects entered year value
c_year=int(datetime.date.today().strftime("%Y"))
def check_year(y):
    try:
        if len(str(y))==2:
            if int(y)>int(str(c_year)[-2:]):
                y='19'+str(y)
            else:
                y='20'+str(y)
        elif int(y)>c_year or int(y)<int(2000):
            print("data only available from "+str(2000)+" to "+str(c_year))
        else:
            pass
        return str(y)
    except:
        print("year input not valid")

"""
#user enters date range

f_date=input("From: mm/dd/yyyy: ").split("/")
f_m=int(f_date[0])
f_d=int(f_date[1])
f_y=int(f_date[2])

check_day(f_d)
check_month(f_m)
check_year(f_y)

t_date=input("To: mm/dd/yyyy: ").split("/")
t_m=int(t_date[0])
t_d=int(t_date[1])
t_y=int(t_date[2])

check_day(t_d)
check_month(t_m)
check_year(t_y)

"""
#Testing block
f_d=int(4)
f_m=int(5)
f_y=int(2010)

t_d=int(17)
t_m=int(10)
t_y=int(2010)
#

f_date=datetime.datetime(f_y,f_m,f_d)
t_date=datetime.datetime(t_y,t_m,t_d)

def d_strip(x):
    return datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
dfs=[]
print("compiling in process, please wait a moment.")
while f_date<=t_date:
    f_date += relativedelta(months=1)
    y=str(d_strip(str(f_date)).year)
    m=str(d_strip(str(f_date)).month-1)
    year=check_year(int(y))
    month=check_month(int(m))
    try:
        dfs.append(pd.read_csv('http://pubdata.mlml.calstate.edu/mlml_last/weather/'+year+"-"+month+".csv"))
    except:
        pass

c_df = pd.concat(dfs, ignore_index=True)

c_df['pst_time']=pd.to_datetime(c_df['pst_time'])
c_df[(c_df['pst_time']>=f_date)&(c_df['pst_time']<=t_date)]

print("Done! Check your downloads folder for the csv file.")
