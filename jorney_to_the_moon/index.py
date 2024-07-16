from collections import defaultdict
def form_related_astronauts(astronauts:list) -> defaultdict:
        
        astronauts_dict = defaultdict(set)
        
        for astronaut in astronauts:
            astronauts_dict[astronaut[0]].add(astronaut[1])
            astronauts_dict[astronaut[1]].add(astronaut[0])
        
        return astronauts_dict
    
def get_astronauts_by_countries(n, astronauts):
    
    by_countries = []
    visited_astronauts = [False] * n
    for astronaut_number in range(n):
        same_country_astronauts = set()
        if astronauts.get(astronaut_number) and not visited_astronauts[astronaut_number]:
            same_country_astronauts = get_related_astronauts(astronaut_number, astronauts)
            visited_astronauts = [True if index in same_country_astronauts else value for index,value in enumerate(visited_astronauts)]
            by_countries.append(same_country_astronauts)
    return by_countries

