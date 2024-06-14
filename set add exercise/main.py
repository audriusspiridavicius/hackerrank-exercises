
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


def main():
    stamps = get_data()
    
    unique_stamps = get_unique_stamps(stamps)
    print(len(unique_stamps))


if __name__ == "__main__":
    main()