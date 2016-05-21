from datetime import date,datetime
import datetime

present_date = datetime.date.today()
yesterday = present_date + datetime.timedelta(days=-1)

print(present_date)