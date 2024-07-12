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
    elif (match_index + 1 == s_length and match_index + 1 == t_length):
        if k % 2 == 0:
            operations_count = k
        match_index = -1
    elif match_index == 0 and t_length == 1:
        operations_count = k
    elif match_index > -1:
        operations_count = (t_length - (match_index + 1)) + (s_length - (match_index + 1))
        


    if operations_count == k or (operations_count <= k and match_index == -1) or (operations_count < k and match_index > -1 and (k - operations_count ) % 2 ==0):
        return "Yes"
    else:
        return "No"
    
    
if __name__ == "__main__":
    print(appendAndDelete("aaa","aaa",10))
    print(appendAndDelete("aaa","a",5))
    print(appendAndDelete("a","ab",2))
    # print(appendAndDelete("abc","acf",3))
    # print(appendAndDelete("hackerhappy","hackerrank",9))
    # print(appendAndDelete("cackerhappy","hackerrank",21))
    print(appendAndDelete("abcd","abcdert",10))
    print(appendAndDelete("aaaaaaaaaa","aaaaa",7))

        