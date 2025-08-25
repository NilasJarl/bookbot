from stats import word_count
from stats import character_count
from stats import sort_characters

def get_book_text(file_path):
    #Get the book from the path
    with open(file_path) as book:
        #return the content of the book
        return book.read()
    

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_count(text)
    sorted_characters = sort_characters(character_count(text))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for list in sorted_characters:
        print(f"{list["char"]}: {list["num"]}")
    print("============= END ===============")
    

main()
