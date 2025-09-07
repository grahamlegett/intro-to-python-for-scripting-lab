# Takes input of 2 numbers and operator from user
first_num = int(input("Enter a whole number: "))
second_num = int(input("Enter another whole number: "))
operator = input("Enter an operator *,+,-,or/: ")

print("The result is : ")

if operator == "+": #checks what type of operator
    print(first_num, operator, second_num, "=")
    print(first_num + second_num)
elif operator == "*":
    print(first_num, operator, second_num, "=")
    print(first_num * second_num)
elif operator == "-":
    if first_num >= second_num: #checks if first number is bigger or smaller than second
        print(first_num, operator, second_num)
        print(first_num - second_num)
    if second_num >= first_num:
        print(second_num, operator, first_num)
        print(second_num - first_num)
elif operator == "/":
    if first_num >= second_num:
        print(first_num, operator, second_num)
        possible = float(first_num / second_num) #assigns result to float just in case of decimal answer
        print(possible)
    if second_num >= first_num:
        print(second_num, operator, first_num)
        possible = float(second_num / first_num)
        print(possible)