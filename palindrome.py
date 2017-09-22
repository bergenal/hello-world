def isPalindrome():
    word = raw_input("Enter a word: ")
    original_word = word
    word = word.lower()
    if list(word) == list(word[::-1]):
        print(original_word + " is a palindrome.")
    else:
        print(original_word + " is not a palindrome.")

isPalindrome()
