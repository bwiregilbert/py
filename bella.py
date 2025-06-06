import os
os.system('cls')

print('====Simple Calculator====')
try:
    firstNumber = float(input('Enter the first number: '))
    operator = input('Enter operator (\' + \' , \' * \' , \' / \' , \' - \'): ')
    secondNumber = float(input('Enter the second number: '))
    if operator == "+":
        print(f'Addition of {firstNumber} and {secondNumber} is {firstNumber + secondNumber}')
    elif operator == "*":
        print(f'Multiplication of {firstNumber} and {secondNumber} is {firstNumber * secondNumber}') 
    elif operator == "-":
        print(f'Subtraction of {firstNumber} and {secondNumber} is {firstNumber - secondNumber}')
    elif operator == '/':
        print(f'Division of {firstNumber} and {secondNumber} is {firstNumber / secondNumber}')
    else:
        print('Invalid operator')
                           
except ValueError:
    print('Enter a valid number.')
except ZeroDivisionError:
    print('Can\'t divide by zero')
finally:
    print('Calculation complete.')                 














