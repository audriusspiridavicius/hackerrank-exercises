
def climbingLeaderboard(ranked, player):
    
    ranked = set(ranked)
    player_temp = set(player)
    
    ranked = ranked.union(player_temp)
    
    ranked = sorted(ranked, key= lambda value: -value)

    player_ranks = [ranked.index(score) + 1 for score in player]
    
    return player_ranks


if __name__ == "__main__":
    ranks = climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102])
    print(ranks)