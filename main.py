import sys
from stats import count_words, unique_character_count, sorting_dict, read_book
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = read_book(sys.argv[1])
    counted_words = count_words(book_text)
    dict_char_count = unique_character_count(book_text)
    organized_dict = sorting_dict(dict_char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(counted_words)
    print("--------- Character Count -------")
    for item in organized_dict:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
main()