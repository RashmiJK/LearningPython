# Example file for working with date information
# Examples to work with calendar module

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar

def main():
    # DATE OBJECTS
    # Get today's date from the simple today() method from the
    # date class
    today = date.today()
    print("Today's date is", today)

    print("Date components:", today.day, today.month, today.year)

    print("Today's weekday no:", today.weekday())
    days = ["mon", "tue"," wed", "thu", "fri", "sat", "sun"]
    print("Which is a:", days[today.weekday()])


    today = datetime.now()
    print(today)
    t = datetime.time(datetime.now())
    print(t)

    # formatting date and time
    now = datetime.now()
    print(now.strftime("The current year is : %y"))
    print(now.strftime("%a, %d %B, %y"))
    # locale specific
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale date: %X"))

    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24-hour time: %H:%M"))

    print(timedelta(days=365, hours=5, minutes=1))
    now = datetime.now()
    print("today is:" + str(now))
    print("one year from now it will be : " +
          str(now + timedelta(days=365)))
    print("In 2 days and 3 weeks, it will be " +
          str(now + timedelta(days=2, weeks=3)))
    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d, %Y")
    print("One week ago it was: " + s)

    today = date.today()
    afd = date(today.year, 4, 1)
    if afd < today:
        print("April Fool's day already went by %d days ago" % ((today - afd).days))
        afd = afd.replace(year = today.year+1)

    time_to_afd = afd - today
    print("It's just ", time_to_afd.days, "days until next april fool's day")

    c = calendar.TextCalendar(calendar.MONDAY)
    st = c.formatmonth(2017, 1, 0, 0)
    print(st)

    ht = calendar.HTMLCalendar(calendar.SUNDAY)
    st = ht.formatmonth(2017, 1)
    print(st)

    for i in c.itermonthdays(2017, 8):
        print(i)

    for name in calendar.month_name:
        print(name)

    for day in calendar.day_name:
        print(day)


    print("Team meetings will be on: ")
    for m in range(1,13):
        cal = calendar.monthcalendar(2018, m)
        weekone = cal[0]
        weektwo = cal[1]
        if weekone[calendar.FRIDAY] != 0:
            meetday = weekone[calendar.FRIDAY]
        else:
            meetday = weektwo[calendar.FRIDAY]

        print("%10s %2d" % (calendar.month_name[m], meetday))



if __name__ == "__main__":
    main()