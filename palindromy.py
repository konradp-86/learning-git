def is_palindrome(word):
    original_word = word
    word = word.replace(" ", "").lower()
    if word == word[::-1]:
        print(f"{original_word}: True")
    else:
        print(f"{original_word}: False")
is_palindrome("kajak")  
is_palindrome("potop")  
is_palindrome("python")  
is_palindrome("A to kanapa pana Kota")  