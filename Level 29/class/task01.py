def count_words(text):
    words = text.split()
    return len(words)


text = "ეს არის მაგალითი ტექსტის."
print(count_words(text))  
