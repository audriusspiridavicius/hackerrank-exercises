import math

def remove_spaces(text:str):
    return text.replace(" ","")


def get_enceyption_step(number:int):
    
    sqrt = math.sqrt(number)
    
    step = math.ceil(sqrt)
    
    return step

def get_encrypted_text(text:str):
    
    encrypted_text = ""
    
    step = get_enceyption_step(len(text))
    first_row = text[0:step]
    word_separator = " "
    
    for letter_index,_ in enumerate(first_row):
        index = letter_index
        while index < len(text):
            encrypted_text += text[index]
            index += step
        encrypted_text += word_separator
    return encrypted_text.strip()
                