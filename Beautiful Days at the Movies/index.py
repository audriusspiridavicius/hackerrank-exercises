
def is_beautiful_day(day,k):
    
    day_str = str(day)
    reverse_day = int(day_str[::-1])
    beautiful_day = abs(day - reverse_day) % k == 0

    return beautiful_day

if __name__ == "__main__":
