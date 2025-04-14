import sys
from stats import word_count
from stats import count_char
from stats import sort_list



def get_book_text (path_to_file):
    """Opens and reads from file"""
    with open(path_to_file) as book:
         book_contents = book.read()
    return book_contents

def main ():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = word_count(book_text)
    report_list = sort_list(count_char(book_text))    
    print(f"""
============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------    
    """)
    for item in report_list:
        if item["Character"].isalpha():
            print(f"{item["Character"]}: {item["Number"]}")
    print("============= END ===============") 

main()