with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    count = file_contents.split()
    num_words = len(count)

print(f"Found {num_words} total words")
