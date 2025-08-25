import sys
from stats import word_count
from stats import character_count
from stats import sort_characters


def get_book_text(file_path):
    #Get the book from the path
    with open(file_path) as book:
        #return the content of the book
        return book.read()
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    sorted_characters = sort_characters(character_count(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(text)} total words")
    print("--------- Character Count -------")
    for list in sorted_characters:
        print(f"{list["char"]}: {list["num"]}")
    print("============= END ===============")
    
    

main()
