from time import *
from calendar import *
# discover the Epoch
# current time in UTC
gmtime(0) # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
time() # returns time elapsed since the Epoch in seconds (UTC)
time_ns() # in nano seconds ( int )
ctime(time()) # 'Wed Nov  3 18:19:30 2021'
ctime() # 'Wed Nov  3 18:19:30 2021'
# time tuple
time_tuple = (2021, 11, 3, 18, 44, 0, 2, 300, 0)
# time object
time_obj = struct_time(time_tuple) # it simply structures the time tuple
# Local time
local = localtime()
local.tm_zone # 'W. Central Africa Standard Time'
local.tm_gmtoff # 3600s ( offset from UTC )
local.tm_isdst # 0 (1 if it's day saving time)
def local_time_zone():
    return f"{localtime().tm_zone} UTC-{localtime().tm_gmtoff // 3600} Daylight saving time: {bool(localtime().tm_isdst)}"
mktime(localtime()) # expects local time
mktime(gmtime()) + localtime().tm_gmtoff # using it with gmtime

# converting time to strings
# from floats
ctime(time())
# from tuples
asctime(gmtime())
asctime(localtime()) 