import sys
from stats import get_num_words, get_book_text, get_chars_dictionary, get_filtered_char_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_location = sys.argv[1]
        text = get_book_text(book_location)
        num_words = get_num_words(text)
        chars_dictionary = get_chars_dictionary(text)
        filtered_char_list = get_filtered_char_list(chars_dictionary)
        create_report(book_location, num_words, filtered_char_list)

def create_report(book_location, num_words, filtered_char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")

    for letter in filtered_char_list:
        if letter["char"].isalpha():
            print(f"{letter["char"]}: {letter["num"]}")

    print("============= END ===============")

main()