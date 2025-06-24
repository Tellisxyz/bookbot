def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

from stats import get_book_word_count
from stats import count_characters
from stats import get_sorted_characters


def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    counts = get_sorted_characters(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    number = get_book_word_count(book)
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    for item in counts:
        if item["char"].isalpha() == True:
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
        

main()
