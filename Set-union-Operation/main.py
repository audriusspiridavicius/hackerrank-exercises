def get_data():
    english_sub_count = int(input().strip())
    english_subsc = int(input().strip().split())
    french_sub_count = int(input().strip())
    french_subsc = int(input().strip().split())
    
    return english_subsc, french_subsc
def get_subscibers_count(english, french):
    
    english = set(english)
    french = set(french)
    
    
    return len(english.union(french))
