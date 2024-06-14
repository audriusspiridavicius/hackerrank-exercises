
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