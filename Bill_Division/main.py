# bonAppetit has the following parameter(s):

# bill: an array of integers representing the cost of each item ordered
# k: an integer representing the zero-based index of the item Anna doesn't eat
# b: the amount of money that Anna contributed to the bill



#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    
    
    anna_eat = [item for index,item in enumerate(bill) if index != k]
    
    anna_bill = sum(anna_eat) / 2
    
    if anna_bill == b:
        print("Bon Appetit")
    else:
        print(int(abs(b - anna_bill)))

if __name__ == "__main__":
        bonAppetit([3, 10, 2, 9],1,12)