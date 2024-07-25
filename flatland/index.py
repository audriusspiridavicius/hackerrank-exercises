from functools import reduce


def flatlandSpaceStations(n, c):
    
    distances = []
    
    for city in range(n):
        nearest_station = min([abs(city - station) for station in c])
        distances.append(nearest_station)

    return max(distances)


if __name__ == "__main__":
    flatlandSpaceStations(5,[0,4])
    flatlandSpaceStations(5,[0,4])