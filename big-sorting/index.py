from decimal import Decimal

def print_values(arr):
    for item in arr:
        print(item)

def bigSorting(unsorted):
    sorted_list = sorted(unsorted, key=Decimal)
    return sorted_list

if __name__ == "__main__":
    values = ['5', '1', '1', '19', '15']
    print_values(bigSorting(values))