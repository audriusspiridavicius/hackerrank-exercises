def organizingContainers(containers):
    # Write your code here
    container_sizes = sorted([sum(c) for c in containers])

    types:list[int] = [0 for _ in range(len(containers))]
    for _, container in enumerate(containers):
         for i in range(len(container)):
             types[i] += container[i] 
    types = sorted(types)

    if container_sizes==types:
        return "Possible"
    else:
        return "Impossible"