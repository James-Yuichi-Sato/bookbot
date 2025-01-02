from collections import Counter

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()

print(file_contents)

words_in_frankenstein = file_contents.split()

print(len(words_in_frankenstein))

letters_in_frankenstein = dict(Counter(file_contents.lower()))
print(letters_in_frankenstein)


print(f"{len(words_in_frankenstein)} words found in the document\n\n")
for letter, count in letters_in_frankenstein.items():
    print(f"The '{letter}' character was found {count} times")
