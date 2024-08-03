def addition():
    while True:
        try:
            a = int(input("Please enter the first number for the addition operation: "))
            b = int(input("Please enter the second number: "))
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of adding {a} + {b} = {a + b}")
            break
def subtraction():
    while True:
        try:
            a = float(input("Please enter the first number for the subtraction operation: "))
            b = float(input("Please enter the second number: "))
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of subtracting {a} - {b} = {a - b}")
            break

def division():
    while True:
        try:
            a = float(input("Please enter the first number for the division operation: "))
            b = float(input("Please enter the second number: "))
            ans = a/b
        except ValueError:
            print("Please enter valid numbers!")
        except ZeroDivisionError:
            print("Sorry it is impossible to divide by zero!!!")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of dividing {a} / {b} = {round(ans, 2)}")
            break

def multiply():
    while True:
        try:
            a = float(input("Please enter the first number for the multiplication operation: "))
            b = float(input("Please enter the second number: "))
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of multiplying {a} x {b} = {a * b}")
            break   

while True:
    action = input('''
Select an action you'd like to perform:

1 - Addition
2 - Subtraction
3 - Division
4 - Muliplication
5 - Quit
''')
    if action == "1":
        addition()
    elif action == '2':
        subtraction()
    elif action == '3':
        division()
    elif action == '4':
        multiply()
    elif action == '5':
        pass # quit
        break  