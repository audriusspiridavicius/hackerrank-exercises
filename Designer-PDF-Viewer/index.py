import string

def designerPdfViewer(h, word):
    letters = string.ascii_lowercase
    max_height = 0
    letter_count = len(word)
    
    for letter in word:
        letter_index = letters.find(letter)
        letter_height = h[letter_index]
        if letter_height > max_height:
            max_height = letter_height
    size = letter_count * max_height
    
    return size

if __name__ == "__main__":
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
    word = "zaba"
    print(designerPdfViewer(h,word))