exec(open('./Scrapy_updatedNames.py').read())

s=Sun_expo()
s.data_range(4,5,2010,10,17,2010)
"""

frm=input("Enter the earliest date you want data from (MM/DD/YYYY): ").split("/")
to=input("Enter the latest date you want data from (MM/DD/YYYY): ").split("/")

from_m=int(frm[0])
from_d=int(frm[1])
from_y=int(frm[2])

to_m=int(to[0])
to_d=int(to[1])
to_y=int(to[2])

s.data_range(from_m,from_d,from_y,to_m,to_d,to_y)
"""