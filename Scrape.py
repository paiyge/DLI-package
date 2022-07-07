import pandas as pd
import datetime
import numpy as np
from dateutil.relativedelta import relativedelta

#Checks / corrects entered month value
def check_month(m):
    if m >12 or m<1:
        print("From month: input not valid")
    elif len(str(m)) ==1:
        m='0'+str(m)
    else:
        pass
    return str(m)

#Checks / corrects entered year value
c_year=int(datetime.date.today().strftime("%Y"))
def check_year(y):
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
"""
#user enters date range

f_date=input("From: mm/dd/yyyy: ").split("/")
f_m=int(f_date[0])
f_d=int(f_date[1])
f_y=int(f_date[2])

check_month(f_m)
check_year(f_y)

t_date=input("To: mm/dd/yyyy: ").split("/")
t_m=int(t_date[0])
t_d=int(t_date[1])
t_y=int(t_date[2])

check_month(t_m)
check_year(t_y)
"""
f_d=int(15)
f_m=int(6)
f_y=int(2010)

t_d=int(15)
t_m=int(8)
t_y=int(2010)

f_date=datetime.datetime(f_y,f_m,f_d)
t_date=datetime.datetime(t_y,t_m,t_d)

def d_strip(x):
    return datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
dfs=[]
while f_date<=t_date:
    print(f_date)
    f_date += relativedelta(months=1)
    y=str(d_strip(str(f_date)).year)
    m=str(d_strip(str(f_date)).month-1)
    year=check_year(int(y))
    print(year)
    month=check_month(int(m))
    print(month)
    try:
        dfs.append(pd.read_csv('http://pubdata.mlml.calstate.edu/mlml_last/weather/'+year+"-"+month+".csv"))
    except:
        pass
    
print(dfs) 
#comp_df = pd.concat(dfs, ignore_index=True)
#comp_df.to_csv("/Users/marinwitherspoon/Downloads/comp_data.csv")
