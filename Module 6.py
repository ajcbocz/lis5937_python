import sys
import datetime

def main():
    dt = datetime.now()
    # utc = datetime.utcnow()
    time_string = dt.strftime("%X")
    """https://strftime.org"""
    for line in sys.stdin:
        data = line.strip().split("\t")
        print(data)
        if len(data) == 6:
            current_time = datetime.now().strftime("%c")
            date, _time, store, item, cost, payment = data
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(date, _time, store, item, cost, payment, current_time))
main()

#Attempt 2

import sys
from datetime import datetime
from datetime import time
from datetime import date
def main():

    dt = datetime.now()
   #utc = datetime.utcnow()
    time_string = dt.strftime("%X")
    """https://strftime.org"""

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            _date, _time, store, item, cost, payment = data
            print ("{0}\t{1}".format(item, cost))


main()

from datetime import datetime, date, time, timezone

datetime.now()

d = timedelta(microseconds=-1)
(d.days, d.seconds, d.microseconds)