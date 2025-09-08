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

# Problem 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a
# user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative 
#   numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting
#   age.
# - Print a message indicating whether the user is eligible to vote based on the
#   entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure that you handle any 
#   conversion errors gracefully. You may need to look up how to do this online.
# - Use a conditional statement to check if the age meets the minimum voting age
#   requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    voting_age = 18
    age = input("Please enter your age: ")
    try:
        entered_age = int(age)
    except ValueError as e:
        print(f"Error: {e}"); 

    if entered_age > 0 and entered_age <= 17:
        print("You are NOT eligible to vote!")
    elif entered_age > 0 and entered_age >= voting_age:
        print("You ARE eligible to vote!")
    else: 
        print("INVALID ENTRY!!")  
              



# Call the function
check_voting_eligibility()

# Problem 3: Calculate dog years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's
# age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the
#   dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog_age = input("Enter dog's age: ")
    try:
        dog_entered = int(dog_age)
    except ValueError as e:
        print(f"Error: {e}");   
    if dog_entered > 0 and dog_entered > 2:
        year_dog = ((10 * 2) + ((dog_entered - 2) * 7))
        print("The dog's age in dog years is: ")
        print(year_dog)
    elif dog_entered < 2 and dog_entered > 0:
        print("The dog is 10 years old in dog years")
    else:
        print("Sorry to say you don't have a dog")

# Call the function
calculate_dog_years()
