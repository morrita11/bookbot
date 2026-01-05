
# get word total 
def get_num_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count = file_contents.split()
        num_words = len(count)
    print(f" - Found {num_words} total words")
get_num_words()
# cont lesters 
def word_cont():
    t_con = 0
    e_con = 0
    with open("books/frankenstein.txt") as f:
        book = f.read()
        book_low = book.lower()
        letters = list(book_low)
        for i in range(0,len(letters)):
            if letters[i] == "t":
                t_con += 1
            if letters[i] == "e":
                e_con += 1
    print(f" - ''e: {e_con}'")
    print(f" - ''t: {t_con}'")
word_cont()