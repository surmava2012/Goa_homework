def count_words(text):

    words = text.split()
    return len(words)

text = "გამარჯობა, როგორ ხარ?"
print(count_words(text))  
