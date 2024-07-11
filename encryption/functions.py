import math

def remove_spaces(text:str):
    return text.replace(" ","")


def get_grid_dimensions(number:int):
    
    sqrt = math.sqrt(number)
    
    rows = math.floor(sqrt)
    columns = math.ceil(sqrt)
    
    return rows, columns


def text_to_grid(text, rows, columns):
    
    grid_array = []
    column = 0
    for _ in range(columns):
        row = [*text[column:column+columns]]
        if row:
            grid_array.append(row)
        column += columns
    
    return grid_array


def get_encrypted_text(grid:list):
    
    encrypted_text = []
    for row_index in range(len(grid[0])):
        wrd = ""
        for index in range(len(grid)):
            if row_index < len(grid[index]):
                wrd += grid[index][row_index]
        encrypted_text.append(wrd)
    
    return " ".join(encrypted_text)
            