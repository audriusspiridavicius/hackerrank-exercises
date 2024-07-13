def countingValleys(path):
    
    valleys = 0
    mountain = 0
    sea_level = 0

    for path_step in path:
        
        if path_step == "U":
            sea_level +=1
        elif path_step == "D":
            sea_level -=1
        
        if sea_level == 0:
            if path_step == "U":
                valleys +=1
            elif path_step == "D":
                mountain +=1
    return valleys

if __name__ == "__main__":
    print(countingValleys(0,"UDDDUDUUUUDDUDDUDU"))