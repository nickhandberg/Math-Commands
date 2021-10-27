#Nicholas Handberg, Assignment 3, 1/27/2021
#Topics: Functions or methods, global variables
#Build a simple command line calculator that supports addition, subtraction, multiplication, division, and absolute value


add_count = 0                                                                                   # function usage count global variables
sub_count = 0
mul_count = 0
div_count = 0
abs_count = 0

def main():                                                                                     # Defines the main() function                                                                              
    parse = 'temp'                                                                              # Assigns a temp string to parse to get the while loop started
    print("Enter command (add, sub, mul, div, abs, quit) followed by the required numbers.")
    while parse[0] != 'quit':                                                                   # While loop that will continue looping until the user's input is quit
        user_input = input(">")                                                                 # Gets the user's input
        parse = user_input.split(" ")                                                           # Parses the user's input

        try:                                                                                    # Try/except, to account for users forgetting to input numbers or inputing the wrong ammount of numbers
            if parse[0] == 'add':                                                               # Checks if the user's command was 'add'
                result = add(float(parse[1]),float(parse[2]))                                   # Passes the numbers as parameters to the add() function and assigns the returned value into to the variable result
            elif parse[0] == 'sub':                                                             # Checks if the user's command was 'sub'
                result = sub(float(parse[1]),float(parse[2]))                                   # Passes the numbers as parameters to the sub() function and assigns the returned value into to the variable result
            elif parse[0] == 'mul':                                                             # Checks if the user's command was 'mul'
                result = mul(float(parse[1]),float(parse[2]))                                   # Passes the numbers as parameters to the mul() function and assigns the returned value into to the variable result
            elif parse[0] == 'div':                                                             # Checks if the user's command was 'div'
                result = div(float(parse[1]),float(parse[2]))                                   # Passes the numbers as parameters to the div() function and assigns the returned value into to the variable result
            elif parse[0] == 'abs':                                                             # Checks if the user's command was 'abs'
                result = abs(float(parse[1]))                                                   # Passes the number as a parameter to the abs() function and assigns the returned value into to the variable result
            elif parse[0] == 'quit':                                                            # Checks if the user's command was 'quit' and passes 
                pass
            else:
                print("Please enter a valid command (add,sub,mul,div,abs)")                     # Otherwise the user did not enter a valid command and asks them to re-enter
            if parse[0] in ('add','sub','mul','div','abs'):                                     # If the command was valid, prints the result to the user's display
                print(result)            
        except IndexError or ValueError:                                                        # Except to give instruction to the user if they entered the wrong ammount of numbers or values.
            print("Enter two numbers for: add, sub, mul, div\nOne number for: abs")
            print("Seperated by single spaces.")
        

    print_stats()                                                                               # Once the while loop is broken, calls the print_stats() function
        

def add(num1, num2):                                                                            # Defines add() with parameters num1 and num2
    global add_count                                                                            # Defines add_count as a global variable and adds 1 to the total
    add_count += 1
    return num1 + num2                                                                          # Sums the two parameters and returns the result

def sub(num1, num2):                                                                            # Defines sub() with parameters num1 and num2
    global sub_count                                                                            # Defines sub_count as a global variable and adds 1 to the total
    sub_count += 1
    return num1 - num2                                                                          # Subtracts the first paramater by the second and returns the result

def mul(num1, num2):                                                                            # Defines mul() with parameters num1 and num2
    global mul_count                                                                            # Defines mul_count as a global variable and adds 1 to the total
    mul_count += 1
    return num1 * num2                                                                          # Multiplies the two parameters and returns the result

def div(num1, num2):                                                                            # Defines div() with parameters num1 and num2
    global div_count                                                                            # Defines div_count as a global variable and adds 1 to the total
    div_count += 1
    if num2 == 0:                                                                               # If the second parameter is equal to zero, prints ERROR: Division by zero and returns a value of 0
        print("ERROR: Division by zero")
        return 0
    else:                                                                                       # Otherwise divides the first parameter by the second and returns the result
        return num1 / num2

def abs(num1):                                                                                  # Defines abs() with parameter num1
    global abs_count                                                                            # Defines abs_count as a global variable and adds 1 to the total 
    abs_count += 1
    if num1 <= 0:                                                                               # If the parameter is negative, multiplies it by -1 to make it positive and returns the value
        return num1 * -1
    return num1                                                                                 # Otherwise just returns the same value passed into the function

def print_stats():                                                                              # Defines print_stats() function
    print(f"add function :{add_count}")                                                         # Prints the count values for add, sub, mul, div, and abs to the user's display
    print(f"sub function :{sub_count}") 
    print(f"mul function :{mul_count}") 
    print(f"div function :{div_count}")
    print(f"abs function :{abs_count}") 

    
main()                                                                                          # Calls the main() function