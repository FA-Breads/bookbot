import sys
from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    characters = character_count(text)
    characters = sorted_list(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in characters:
        ch = item["char"]
        count = item["num"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {count}")


    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()