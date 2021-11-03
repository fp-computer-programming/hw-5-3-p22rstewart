# Author RTS 11/3/21

import calendar

# Question 1 
calendar.TextCalendar().pryear(2020)

# Question 2
calendar.TextCalendar(calendar.SUNDAY).pryear(2020)

# Question 3
calendar.TextCalendar().prmonth(2004, 8)

# Question 4
calendar.LocaleTextCalendar(6, "SPANISH").pryear(2020)

# Question 5 
print(calendar.isleap(2004))
