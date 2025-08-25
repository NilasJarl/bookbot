def word_count(text):
    #return the word count of text
    return len(text.split())

#function that takes a text/string and counts the number of charaters.
def character_count(text):
    characters = {}
    new_text = text.lower()
    for char in new_text:
        if not char in characters:
            characters[char] = 0
        characters[char] +=1
    return characters

def sort_on(items):
    return items["num"]

def sort_characters(characters):
    sorted_characters = []
    for char in characters:
        if char.isalpha():
            sorted_characters.append({"char": char, "num": characters[char]})
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters
    
    
