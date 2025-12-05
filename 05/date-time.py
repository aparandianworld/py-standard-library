from datetime import date, time, datetime, timedelta

today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)


manual_time = time(10, 56, 00)
print(manual_time)

now = datetime.now()
print(now)
print(now.strftime("%A, %B %d, %Y %I:%M %p"))

one_year = timedelta(days=365)
one_month = timedelta(days=30)
one_week = timedelta(days=7)
one_day = timedelta(days=1)

print("one year from now: ", now + one_year)
print("one week from now: ", now + one_week)
print("one month from now: ", now + one_month)
print("one day from now: ", now + one_day)
print("one week ago: ", now - one_week)


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[now.weekday()])
