def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    text = text.lower()
    characters = {}
    for ch in text:
        characters[ch] = characters.get(ch,0) + 1
    return characters

def sort_by(item):
    return item["num"]

def sorted_list(characters):
    char_list = []
    for ch, count in characters.items():
        char_list.append({"char": ch, "num": count})
    char_list.sort(reverse=True, key=sort_by)
    return char_list
