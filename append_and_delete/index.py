def appendAndDelete(s:str, t:str, k:int):
    
    s_length = len(s)
    t_length = len(t)
    
    shorter_word = min(s_length, t_length)
    match_index = -1
    
    for index in range(shorter_word):
        if s[index] == t[index]:
            match_index = index
        else:
            break
    
    operations_count = 0
    
    if match_index == -1:
        operations_count = s_length + t_length
    elif match_index > -1:
        operations_count = (t_length - (match_index + 1)) + (s_length - (match_index + 1))
    
    if operations_count <= k:
        return "Yes"
    else:
        return "No"
    
    
if __name__ == "__main__":
    print(appendAndDelete("abc","dcf",5))
    print(appendAndDelete("abc","acf",3))
    print(appendAndDelete("hackerhappy","hackerrank",10))
    print(appendAndDelete("cackerhappy","hackerrank",21))

        