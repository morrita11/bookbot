

def get_num_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count = file_contents.split()
        num_words = len(count)
    print(f"Found {num_words} total words")

get_num_words()

def word_cont():
    t = 0
    with open("books/frankenstein.txt") as f:
        book_low =[f.lower()]
        for i in book_low:
            if book_low(i) = "t":