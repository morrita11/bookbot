# exempal of book bot for boots for helping with code 
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

 # exempal of the reading code 
def get_book_text(path):
    with open(path) as f:
        return f.read()

# exempel of the number of words code 
def get_num_words(text):
    words = text.split()
    return len(words)


main()
# form odd lesson 
def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    count = 0
    unique = set()
    for char in text:
        if char in vowels:
            count += 1
            unique.add(char)
    return count, unique