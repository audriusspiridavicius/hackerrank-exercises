def get_board_squares(queen_position:tuple[int,int], board_size:int, row_step, column_step, obstacles:list[tuple[int,int]] = []):

    """Returns a list of squares that the queen can atack"""
    row = queen_position[0]
    column = queen_position[1]
    square_list = []
    
    
    while True:
        
        row = row + row_step
        column = column + column_step
        
        if row > board_size or row < 1:
            break
        
        if column > board_size or column < 1:
            break
        
        cordinates = (row, column)
        
        if cordinates in obstacles:
            break
        
        square_list.append((row, column))
    
    return square_list
        
        
def queensAttack(n, k, r_q, c_q, obstacles):
    
    obstacles = set(obstacles)
    queen_attack_squares = []
    
    queen_position = (r_q, c_q)
    
    queen_attack_squares.append(get_board_squares(queen_position, n, 0, 1, obstacles)) # queens position right
    queen_attack_squares.append(get_board_squares(queen_position, n, 0, -1, obstacles)) # queens position left
    queen_attack_squares.append(get_board_squares(queen_position, n, 1, 0, obstacles)) # queens position up
    queen_attack_squares.append(get_board_squares(queen_position, n, -1, 0, obstacles)) # queens position down
    
    queen_attack_squares.append(get_board_squares(queen_position, n, 1, 1, obstacles)) # queens position diagonal up right
    queen_attack_squares.append(get_board_squares(queen_position, n, 1, -1, obstacles)) # queens position diagonal up left
    
    queen_attack_squares.append(get_board_squares(queen_position, n, -1, -1, obstacles)) # queens position diagonal down left
    queen_attack_squares.append(get_board_squares(queen_position, n, -1, 1, obstacles)) # queens position diagonal down right
    
    queen_attack_squares = sum([len(values) for values in queen_attack_squares])
    
    return queen_attack_squares

if __name__ == "__main__":
    print(f"result = {queensAttack(5,3,4,3,[(5,5),(4,2),(2,3)])}")
    print(f"result = {queensAttack(4,0,4,4,[])}")
   