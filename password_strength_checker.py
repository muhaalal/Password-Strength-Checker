special_characters=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", ":", ";", "'", "<", ">", ",", ".", "?"]
uppercase_letters= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "j", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers= ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
lowercase_letters= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("Let's find out if your password is strong or not")
while True:
    password=input("Enter your password: ")
    if len(password) < 8:
        print("You should have atleast 8 characters, try again please")
    else:
        break


has_upper=any(character in uppercase_letters for character in password)
has_lower=any(character in lowercase_letters for character in password)
has_number=any(character in numbers for character in password)
has_special_letters=any(character in special_characters for character in password)

strength_tester=has_upper + has_lower + has_number + has_special_letters

if strength_tester == 4:
    print("Your password is very Strong")
elif strength_tester == 3:
    print("Your password is strong")
elif strength_tester == 2:
    print("Your password is moderate")
else:
    print("Your password is weak")

