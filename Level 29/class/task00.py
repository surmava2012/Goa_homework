def search(text, word):
    if word in text:
        return "მოსაძებნი სიტყვა არსებობს"
    else:
        return "მოსაძებნი სიტყვა არ არსებობს"

# ნიმუში
text = "ეს არის შესანიშნავი"
word = "შესანიშნავი"

# შედეგი
result = search(text, word)
print(result)
