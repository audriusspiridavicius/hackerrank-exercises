from itertools import permutations 

def formingMagicSquare(s):
    # The magic constant of a normal magic square depends only on n and has the following value: 
    # M = n(n2+1)/2
    n = len(s)
    m = n * (n * n + 1)/2 
    all_permutations = permutations(range(1, (n * n) + 1))       
    
    
    
    rows_sum_filtered = [row for row in all_permutations if sum(row[:3])==m and sum(row[3:6])==m and sum(row[6:9])==m]
    columns_sum_filtered = [column for column in rows_sum_filtered if sum(column[0::3])==m and sum(column[1::3])==m and sum(column[2::3])==m]
    diagonal_sum_filtered = [diagonal for diagonal in columns_sum_filtered if sum(diagonal[0::4])==m]

        
    sum_values_filtered = [list(diagonal) for diagonal in diagonal_sum_filtered if sum(diagonal[2:n*n-1:2])==15]
    
    s2 = []
    for i in range(0,n):
        for j in range(0,n):
            s2.append(s[i][j])
    
    min_v = float("inf")
    for i, value in enumerate(sum_values_filtered):
        summ = sum([abs(s2[index]-v) for index,v in enumerate(value)])
        if summ < min_v:
            min_v = summ     

    return min_v
    # Write your code here

if __name__ == "__main__":
    # formingMagicSquare([[5, 3, 4], [1, 5, 8], [6, 4, 2]])
    formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]])