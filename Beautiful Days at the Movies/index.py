
def is_beautiful_day(day,k):
    
    day_str = str(day)
    reverse_day = int(day_str[::-1])
    beautiful_day = abs(day - reverse_day) % k == 0

    return beautiful_day

def beautifulDays(i, j, k):
    
    beautiful_days_count = 0
    
    for day in range(i,j+1):
        if is_beautiful_day(day,k):
            beautiful_days_count += 1
            
    return beautiful_days_count
    
    
    
    
if __name__ == "__main__":
    print(beautifulDays(1,15,3))