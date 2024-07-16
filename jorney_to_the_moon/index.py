def form_related_astronauts(astronauts:list) -> defaultdict:
        
        astronauts_dict = defaultdict(set)
        
        for astronaut in astronauts:
            astronauts_dict[astronaut[0]].add(astronaut[1])
            astronauts_dict[astronaut[1]].add(astronaut[0])
        
        return astronauts_dict
