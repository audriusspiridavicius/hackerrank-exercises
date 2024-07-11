from functions import remove_spaces, get_grid_dimensions, text_to_grid, get_encrypted_text

def encryption(text):
    
    no_spaces_text = remove_spaces(text)
    
    text_length = len(no_spaces_text)
    
    rows, columns = get_grid_dimensions(text_length)
    
    
    grid = text_to_grid(no_spaces_text, rows, columns)
    
    enc_text = get_encrypted_text(grid)
    return enc_text