a = input("Enter a string: ")
if a in ['a','e','i','o','u','A','E','I','O','U']:
    print("Vowel")
elif a.isalpha():
    print("Consonant")
else :
    print("Invalid charecter ")