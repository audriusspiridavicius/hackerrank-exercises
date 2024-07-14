#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):

    max_subset_len = 0

    for _, number in enumerate(s):
        
        divisible_subset = set() 
        divisible_subset.add(number)
        for next_number in s:
            divisible = False
            for ll in divisible_subset:
                if (ll + next_number) % k == 0:
                    divisible = True
                    break
            if not divisible:
                divisible_subset.add(next_number)
            
        if len(divisible_subset) > max_subset_len:
            max_subset_len = len(divisible_subset)
    
    return max_subset_len
    


if __name__ == "__main__":
    print(nonDivisibleSubset(3, [1, 7, 2, 4]))
