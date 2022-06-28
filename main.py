import time
import os

size = os.get_terminal_size()
for i in range(size.lines):
    print()
os.system('clear')

timeUp = False

totalSeconds = 0
print('0 Years | 0  Months | 0  Weeks | 0  Days | 0  Hours | 0  Minutes | 0  Seconds')

while True:
    time.sleep(1)
    os.system('clear')
    totalSeconds += 1
    years = int(totalSeconds / 31557600)
    months = int(totalSeconds / 2628000 - 12*years)
    weeks = int(totalSeconds / (7*24*60*60) - 12*4*years - 4*months)
    days = int(totalSeconds / (24*60*60) - 12*4*7*years - 4*7*months - 7*weeks)
    hours = int(totalSeconds / (60*60) - 12*4*7*24*years - 4*7*24*months - 7*24*weeks - 24*days)
    minutes = int(totalSeconds / 60 - 12*4*7*24*60*years - 4*7*24*60*months - 7*24*60*weeks - 24*60*days - 60*hours)
    seconds = int(totalSeconds - 12*4*7*24*60*60*years - 4*7*24*60*60*months - 7*24*60*60*weeks - 24*60*60*days - 60*60*hours - 60*minutes)
    
    if years == 1:
        years = str(years) + '  Year '
    else:
        if years > 99:
            timeUp = True
        elif years > 9:
            years = str(years) + ' Years '
        else:
            years = str(years) + '  Years'

    if months == 1:
        months = str(months) + '  Month '
    else:
        if months > 9:
            months = str(months) + ' Months '
        else:
            months = str(months) + '  Months'

    if weeks == 1:
        weeks = str(weeks)+'  Week '
    else:
        weeks = str(weeks)+'  Weeks'

    if days == 1:
        days = str(days)+'  Day '
    else:
        days = str(days)+'  Days'

    if hours == 1:
        hours = str(hours)+'   Hour '
    else:
        if hours > 9:
            hours = str(hours)+' Hours '
        else:
            hours = str(hours)+'  Hours'

    if minutes == 1:
        minutes = str(minutes)+'  Minute '
    else:
        if minutes > 9:
            minutes = str(minutes)+' Minutes '
        else:
            minutes = str(minutes)+'  Minutes'

    if seconds == 1:
        seconds = str(seconds)+'  Second '
    else:
        if seconds > 9:
            seconds = str(seconds)+' Seconds '
        else:
            seconds = str(seconds)+'  Seconds'

    if timeUp != True:
        years, months, weeks, days, hours, minutes, seconds = str(years), str(months), str(weeks), str(days), str(hours), str(minutes), str(seconds)

        print(years+' | '+months+' | '+weeks+' | '+days+' | '+hours+' | '+minutes+' | '+seconds)
    else:
        print("OH NO! How on earth did you manage this!? You've reached the time limit!")
        print("SELF DESTRUCT IN:")
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print('BOOM!')
        exit()