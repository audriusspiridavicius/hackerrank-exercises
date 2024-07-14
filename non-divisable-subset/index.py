#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):

    remainder_counts = [0] * k
    
    for number in s:
        remainder_counts[number % k] += 1
    max_subset_len = 0
    

    if remainder_counts[0] > 0:
        max_subset_len += 1
    
    for i in range(1, (k // 2) + 1):
        if i == k - i: 
            if remainder_counts[i] > 0:
                max_subset_len += 1
        else:
            max_subset_len += max(remainder_counts[i], remainder_counts[k - i])
    
    return max_subset_len
    


if __name__ == "__main__":
    print(nonDivisibleSubset(3, [1, 7, 2, 4]))
