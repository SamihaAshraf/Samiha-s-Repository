#Samiha Ashraf
#1884227
def strengthen_password(password):
    replacements = {'i': '!', 'a': '@', 'm': 'M', 'B': '8', 'o': '.'}
    for char, replacement in replacements.items():
        password = password.replace(char, replacement)
    password += 'q*s'
    return password

input_password = input("")
strong_password = strengthen_password(input_password)
print(strong_password)