exec(open('./Scrapy_updatedNames.py').read())

if __name__ == "__main__":
    cammands=[(4,5,2010,10,17,2010),("June",5,2010,10,17,2010),(4,5,10,10,17,10),
              (4,50,2010,10,17,2010),(5,2010,10,17,2010)]
    #examples of [missing data inside range, string instead of int, abreviated year,
    #miss type from day, skipped from month]
    #[True, False, True, False, False]
    
    #datetime handels a lot of the errors!
    
    s=Sun_expo()
    rate=[]
    for f in cammands:
        try:
            s.data_range(*f)
            rate.append("Pass")
            continue
        except Exception as e:
            print("Error:", e)
            rate.append("Fail")
            continue

    print(rate)
