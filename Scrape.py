import pandas as pd
import datetime

"""
#user enters date range
f_date=input("From: mm/dd/yyyy: ").split("/")
print(f_date)
f_month=int(f_date[0])
print(f_month)
f_day=int(f_date[1])
print(f_day)
f_year=int(f_date[2])
print(f_year)


t_date=input("To: mm/dd/yyyy: ").split("/")
print(t_date)
t_month=int(t_date[0])
print(t_month)
t_day=int(t_date[1])
print(t_day)
t_year=int(t_date[2])
print(t_year)
"""

#testing block
f_day=int(15)
f_month=int(4)
f_year=int(2010)

t_day=int(15)
t_month=int(5)
t_year=int(2010)
#

#Checks entered month value
def check_month(m):
    if m >12 or m<1:
        print("From month: input not valid")
    elif len(str(m)) ==1:
        m='0'+str(m)
        
    else:
        pass
    return m

#Checks entered year value
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
    return y

f_month=check_month(f_month)
f_year=check_year(f_year)

t_month=check_month(t_month)
t_year=check_year(t_year)

url='http://pubdata.mlml.calstate.edu/mlml_last/weather/'+str(f_year)+"-"+str(f_month)+".csv"
print(url)
df=pd.read_csv(url)
print(df)
