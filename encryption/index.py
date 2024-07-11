from functions import remove_spaces, get_encrypted_text

def encryption(text):
    
    no_spaces_text = remove_spaces(text)
    
    enc_text = get_encrypted_text(no_spaces_text)
    return enc_text