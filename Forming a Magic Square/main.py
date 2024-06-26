

def formingMagicSquare(s):
    # The magic constant of a normal magic square depends only on n and has the following value: 
    # M = n(n2+1)/2
    n = len(s)
    m = n * (n * n + 1)/2
    
    for i in range(n):
        for j in range(n):
            line_sum = sum(s[i])
            column_sum = sum([s[z][j] for z in range(n)])
            if line_sum != m and line_sum == column_sum:
               s[i][j] = int(s[i][j] + m - line_sum)          
    
    # Write your code here

if __name__ == "__main__":
    formingMagicSquare([[5, 3, 4], [1, 5, 8], [6, 4, 2]])