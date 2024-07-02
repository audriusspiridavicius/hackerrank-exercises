
def is_divisible(number:int, values:list):
    """Return True if a number is divisible by all values in a list."""
    for value in values:
        if number % value != 0:
            return False
    return True


def is_factorial_all_b(number,values):
    
    for value in values:
        if value % number != 0:
            return False
    return True
    

def getTotalX(a, b):
    
    result_divides_by_a = []
    result_b_factorials = []
    
    for number in range(1,101,1):
        if is_divisible(number, a):
            result_divides_by_a.append(number)
    
    for number in result_divides_by_a:
        if is_factorial_all_b(number, b):
            result_b_factorials.append(number)
            
    return len(result_b_factorials)
        
    
if __name__ == "__main__":
    a = [2, 4]
    b = [16, 32, 96]
    print(getTotalX(a, b))