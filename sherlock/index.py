
import sys
sys.set_int_max_str_digits(60000) 

def decentNumber(n):
    # Write your code here
    possible_3s = []
    possible_5s = []
    
    for number in range(n,1,-1):
        if number % 5 == 0:
            possible_3s.append(number)
        if number % 3 == 0:
            possible_5s.append(number) 
    
    possible_5s.append(0)
    possible_3s.append(0)
    
    
    decent_number_values = set([0])
    br = False
    for possible_5 in possible_5s:
        for possible_3 in possible_3s:
            if possible_3 + possible_5 == n:
                br = True
                decent_number_values.add("3"*possible_3 + "5"*possible_5)
                decent_number_values.add("5"*possible_5 + "3"*possible_3)
            if br:
                break
        if br:
            break

    
    
    decent_number_values = [int(number) for number in decent_number_values]
    max_combination = max(decent_number_values)
    if max_combination == 0:
        return "-1"
    else:
        return int(max_combination)

if __name__ == "__main__":
    print(decentNumber(57634))