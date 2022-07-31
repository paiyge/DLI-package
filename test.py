from re import X


exec(open('./Scrapy_updatedNames.py').read())

if __name__ == "__main__":
    for f in X:
        """
        for fn in (do, do2, do3, do4):
    try:
        fn()
        break
    except:
        continue
        """
    s=Sun_expo()
    #data_range(from month, from day, from year, to_month, to_day, to_year)
    print("example of intended use:")
    s.data_range(4,5,2010,10,17,2010) #Done!

    #if string entered for month:
    print("string error:")
    s.data_range("June",5,2010,10,17,2010) #an integer is required

    #if year is abbreviated:
    print("shortened year error: ")
    s.data_range(4,5,2010,10,17,2010) #an integer is required