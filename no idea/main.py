def get_input():
    return input().strip().split()

def get_data():
    n, m = get_input()
    numbers_array = get_input()
    like_numbers = get_input()
    dislaike_numbers = get_input()
    return numbers_array, like_numbers, dislaike_numbers


def get_happiness(numbers:list,numbers_like:list, numbers_dislike:list):
    
    if len(numbers_like) != len(numbers_dislike):
        return ValueError(" likeable and dislikable arrays are not the same size!")
    
    happiness = 0
    
    size = len(numbers_like)
    
    numbers_like = set(numbers_like)
    numbers_dislike = set(numbers_dislike)
    
    for index in range(size):
        
        likeable_count = numbers.count(numbers_like[index])
        dislikeable_count = numbers.count(numbers_dislike[index])
        
        if likeable_count > 0:
            happiness += likeable_count
    
        if dislikeable_count > 0:
            happiness -= dislikeable_count
    
    return happiness
def main():
    numbers, like_numbers, dislaike_numbers = get_data()
    hapiness_level = get_happiness(numbers, like_numbers, dislaike_numbers)
    print(hapiness_level)


if __name__ == "__main__":
    main()
    pass