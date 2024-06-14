def get_input():
    return input().strip().split()

def get_data():
    n, m = get_input()
    numbers_array = get_input()
    like_numbers = set(get_input())
    dislaike_numbers = set(get_input())
    return numbers_array, like_numbers, dislaike_numbers


def get_happiness(numbers:list,numbers_like:set, numbers_dislike:set):
    
    if len(numbers_like) != len(numbers_dislike):
        raise ValueError(" likeable and dislikable arrays are not the same size!")
    if not numbers:
        raise ValueError("no number")
    
    happiness = 0
    
    for number in numbers:
        
        if number in numbers_like:
            happiness += 1
        
        if number in numbers_dislike:
            happiness -= 1
        
    return happiness

def main():
    numbers, like_numbers, dislaike_numbers = get_data()
    hapiness_level = get_happiness(numbers, like_numbers, dislaike_numbers)
    print(hapiness_level)


if __name__ == "__main__":
    main()