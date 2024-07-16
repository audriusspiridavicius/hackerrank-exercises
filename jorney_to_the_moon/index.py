from collections import defaultdict
from functools import reduce


def get_related_astronauts(current_astronaut:int, astronauts:dict):
    
    stack = [current_astronaut]
    
    same_country_astronauts = set()
    while stack:
        current = stack[0]
        same_country_astronauts.add(current)
        related_astronauts = astronauts.get(current)
        
        for related in related_astronauts:
            if related not in same_country_astronauts:
                stack.append(related)
        stack.pop(0)
        
    return same_country_astronauts
                
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

def get_total_combinations(astronaut_groups,n):
    
    rest_countries = n - sum(astronaut_groups)
    
    rest_countries_combinations = reduce(lambda x,y: x + y, range(0,rest_countries)) if rest_countries > 0 else 0

    single_person_countries_combinations = 0
    country_groups_combinations = 0
    for index,group_size in enumerate(astronaut_groups):
        single_person_countries_combinations = single_person_countries_combinations + group_size * rest_countries
        for following_groups in astronaut_groups[index + 1:]:
            country_groups_combinations = country_groups_combinations + group_size * following_groups
        
    total_combinations = country_groups_combinations + single_person_countries_combinations + rest_countries_combinations
    
    return total_combinations


