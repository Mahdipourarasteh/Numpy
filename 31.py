import numpy as np

today= np.datetime64('2020-02-12')
print("Date is:", today)
print("Year is:", np.datetime64(today, 'Y'))

dates= np.arange('2020-02', '2020-03', dtype= 'datetime64[D]')
print("\nDates of February, 2020: \n", dates)
print("Today is February:", today in dates)

dur= np.datetime64('2021-05-22') - np.datetime64('2020-05-22')
print("\nNo. of days:", dur)
print("No. of weeks:", np.timedelta64(dur, 'W'))

a=np.array(['2018-02-12','2019-10-13','2020-05-22'], dtype='datetime64')
print("\nDates in sorted order:", np.sort(a))