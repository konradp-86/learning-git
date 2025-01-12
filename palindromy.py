def is_palindrome(word):
    original_word = word
    word = word.replace(" ", "").lower()
    if word == word[::-1]:
        print(f"{original_word}: True")
    else:
        print(f"{original_word}: False")
word_to_check = input("Jakie słowo sprawdzić? ")
is_palindrome(word_to_check) 