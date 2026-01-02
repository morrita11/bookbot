with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    count = file_contents.split()
    number = len(count)

print(f"Found {number} total wrods")
