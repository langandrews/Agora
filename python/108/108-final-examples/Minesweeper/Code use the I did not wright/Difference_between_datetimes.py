'''
Finds difference in minutes between two datetime objects
Created Fall 2015
@author: ajd74
Based on code by SilentGhost
http://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python
'''

>>> import datetime
>>> a = datetime.datetime.now()
>>> b = datetime.datetime.now()
>>> c = b - a
datetime.timedelta(0, 8, 562000)
>>> divmod(c.days * 86400 + c.seconds, 60)
(0, 8)      # 0 minutes, 8 seconds

