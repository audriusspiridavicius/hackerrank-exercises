
def get_data():
    number_of_stamps = int(input().strip())
    
    data = []
    for _ in number_of_stamps:
        stamp = input().strip()
        data.append(stamp)
    return data

def get_unique_stamps(stamps:list):
    unique_stamps = set(stamps)
    
    return unique_stamps

