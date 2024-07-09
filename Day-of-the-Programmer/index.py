from calendar import monthrange, isleap


def dayOfProgrammer(year):

    programmer_day = 256
    days = 0
    month = 1


    if year == 1918:
        days = days - 13
    
    if year < 1918:
        if year % 4 == 0 and year % 100 ==0:
            days = days + 1

    while True:
        
        month_days = monthrange(year, month)[1]
        if days + month_days > programmer_day:
            break 
        
        days += month_days
        month += 1

    day = programmer_day - days
    
    return f"{day:02}.{month:02}.{year:04}"
    

    
if __name__ == "__main__":
    print(dayOfProgrammer(2016))
    print(dayOfProgrammer(2017))

    print(dayOfProgrammer(1800))
    print(dayOfProgrammer(1836))
