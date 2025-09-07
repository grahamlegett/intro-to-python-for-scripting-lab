# Problem 1: Vowel or consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and 
#   determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user in the above
#   messages.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels. You may need to look up
#   how to use this online.
# - Ensure your code provides feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    CAPS_my_list = ["Q","W","R","T","Y","P","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
    my_list_lower = ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    vowel_list = ["a","e","i","o","u","A","E","I","O","U"]
    letter_check = input("Enter a letter from a-z not case sensitive: ")
    print(type(letter_check))
    if letter_check in CAPS_my_list:
        print("The letter "); print(letter_check); print(" is a consonant")
    elif letter_check in my_list_lower:
        print("The letter "); print(letter_check); print(" is a consonant") 
    elif letter_check in vowel_list:
        print("The letter "); print(letter_check); print(" is a vowel")
    else:
        print("INVALID ENTRY")
    


# Call the function
check_letter()
