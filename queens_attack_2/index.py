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
        
        
