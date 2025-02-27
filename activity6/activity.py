letter = input("Enter a Letter :")

if letter in "aeiou":
    print("Vowel")
elif letter.isalpha() and len(letter) == 1:
    print("Consonant")
else:
    print("Invalid Input")

