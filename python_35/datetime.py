import _datetime
now = _datetime.datetime.now()
n_days =45
mydate =  _datetime.timedelta(days=n_days)
n_day = now + mydate
print('从今天起的{0}天的日期是：'.format(n_days))
print(n_day.strftime('%Y-%m-%d %H:%M:%S'))
print(now.strftime('%Y-%m-%d %H:%M:%S'))
