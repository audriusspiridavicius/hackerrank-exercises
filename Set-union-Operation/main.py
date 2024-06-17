def get_subscibers_count(english, french):
    
    english = set(english)
    french = set(french)
    
    
    return len(english.union(french))
