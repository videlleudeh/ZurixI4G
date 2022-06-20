from ast import Continue


print ("Videlle's CLI Calculator")

print (" ")

calculation = True

while calculation:

    print("Starting Calculator")
    print(" ") 


    try:
        num1 = float(input("Enter a number: "))
        opr = input("+ - / % OR *: ")
        num2 = float(input("Enter another number: "))
    except:
        print ("That is not a nmuber. Retry!")
        continue

    print (" ")


    if opr == "+":
        print (num1 + num2)
    elif opr == "-":
        print (num1 - num2)
    elif opr == "/":
        print (num1 / num2)
    elif opr == "%":
        print (num1 % num2)
    elif opr == "*":
        print (num1 * num2)
    else: 
        print("Syntax error")


    choice = input('Would you like to continue your calculations? Yes/No: ')
   
    if choice == "Yes":
        pass
    if choice == "No":
        calculation = False
        print ("Thanks for using Videlle's Calculator!")
        
 