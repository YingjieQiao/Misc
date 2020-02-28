def leap_year(year):
    if year%4 != 0:
        return False
    elif year%100 != 0:
        return True
    elif year%400 != 0:
        return False
    else:
        return True

def day_of_week_jan1(year):
    return int((1 + 5*((year-1)%4) + 4*((year-1)%100) + 6*((year-1)%400))%7)

def num_days_in_month(month_num, leap_year):
    month = {1: 31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if month_num == 2:
        if leap_year:
            return 29
        else:
            return 28
    else:
        return month[month_num]

def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    #formatting takes time man
    month = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    week1 = "   "*first_day_of_month
    for i in range(7-first_day_of_month):
        week1 += "  " 
        week1 += str(i+1)
        
    out = [month[month_num], week1] #line by line, first line is mon+week1
    n = num_days_in_month - (7-first_day_of_month) #days left
    
    weekn= ""
    i = 0
    while n>0:
        weekn += ' ' 
        
        if num_days_in_month+1-n < 10:
            weekn += ' '
        
        weekn += str(num_days_in_month+1-n)
        i += 1
        n -= 1
        if i == 7:
            out.append(weekn)
            i = 0
            weekn = ''
    if weekn != '':
        out.append(weekn)
    return out

def construct_cal_year(year):
    firstday = day_of_week_jan1(year)
    leap = leap_year(year)
    out = [year]
    for i in range(1,13):
        out.append(construct_cal_month(i, firstday, num_days_in_month(i,leap)))
        
        if len(out[-1][-1]) != 21:
            firstday = int(len(out[-1][-1])/3)
        else:
            firstday = 0
        
    return out

def display_calendar(year):
    ls = construct_cal_year(year)
    out = ''
    for i in range(1,13):
        if i != 1:
            out += '\n\n'
        out += ls[i][0] 
        out += '\n  S  M  T  W  T  F  S'
        for row in ls[i][1:]: #ls[i][0] is name of the month
            out += '\n' + str(row)
    return out
    
print(display_calendar(2020))
