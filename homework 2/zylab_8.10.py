#Samiha Ashraf
#1884227
def is_palindrome(input_string):
    input_string = input_string.replace('', '')

    if input_string == input_string[::-1]:
        return True
    else:
        return False

word = input('')

if is_palindrome(word):
    print(word, 'is a palindrome')
else:
    print(word, 'is not a palindrome')