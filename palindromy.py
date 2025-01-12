def is_palindrome(word):
    original_word = word
    word = word.replace(" ", "").lower()
    if word == word[::-1]:
        print(f"{original_word}: True")
    else:
        print(f"{original_word}: False")
while True:
    word_to_check = input("Jakie słowo sprawdzić? (lub wpisz 'exit', aby zakończyć) ")
    if word_to_check.lower() == 'exit':
        break
    is_palindrome(word_to_check)