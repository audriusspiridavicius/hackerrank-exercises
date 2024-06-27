import time
from collections import OrderedDict

def climbing_leaderboard(ranked, player)-> list:
    player_ranks = []

    unique_scores_leaderboard = list(OrderedDict([(value,index) for index, value in enumerate(ranked)]))
   

    for game in player:
        unique_scores_count = len(unique_scores_leaderboard)
        
        if game < unique_scores_leaderboard[-1]:
            player_ranks.append(unique_scores_count + 1)
            continue
        elif game >= unique_scores_leaderboard[0]:
            player_ranks.append(1)
            continue
        else:
        
            size = unique_scores_count
            
            low = 0
            high = size - 1
            middle= 0
            
            while True:
                
                if abs(low-high) == 1:
                    player_ranks.append(high+1)
                    break
                
                middle = int(low + (high - low) / 2)
                
                if unique_scores_leaderboard[middle] == game:
                    player_ranks.append(middle + 1)
                    break
                elif unique_scores_leaderboard[middle] > game:
                    low = middle
                elif unique_scores_leaderboard[middle] < game:
                    high = middle

    return player_ranks


if __name__ == "__main__":
    
    start_time = time.time()
    ranks = climbing_leaderboard([100, 90, 80, 80, 75, 60], [50, 65, 77, 90, 102])
    print(ranks)
    ranks = climbing_leaderboard([100, 100, 50, 40, 40, 20, 10, 9], [5, 25, 50, 120])
    print("--- %s seconds ---" % (time.time() - start_time))
    print(ranks)