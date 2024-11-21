# Ethan Lawrence
# Nov 20 2024
# math with menu

import math
import time
# Functions:
def calc_circle(radius):
    area = math.pi * radius**2
    return area
# End of calc_circle

def calc_power(base, exponent):
    result = base**exponent
    return result
# End of calc_power

def calc_triangle(base, height):
    area = base * height * 0.5
    return area
# End of calc_triangle

def display_menu():
    print("""\nMenu:
1. Calculate area of a circle
2. Raise a number to a power
3. Calculate area of a right triangle
4. Exit""")
# End of display_menu

def main():
    while True:
        display_menu()
        choice = input('Enter your menu choice:  ')

        if choice == '1':
            num1 = float(input('Enter the radius:  '))
            solution = calc_circle(num1)
            print(f'The area of the circle is: {solution} sq. ft.')
        elif choice == '2':
            num1 = float(input('Enter the base:  '))
            num2 = float(input('Enter the exponent:  '))
            solution = calc_power(num1, num2)
            print(f'{num1} raised to the power of {num2} is: {solution}')
        elif choice == '3':
            num1 = float(input('Enter the base:  '))
            num2 = float(input('Enter the height:  '))
            solution = calc_triangle(num1, num2)
            print(f'The area of a right triangle is: {solution:.2f} sq. ft.')
        elif choice == '4':
            print("Exiting the script...")
            time.sleep(2)
            print("Thank you for using my script today!")
            time.sleep(2)
            print("Goodbye!")
            break
        else:
            print('invalid menu choice! Please enter a number between 1 and 4.')
        print()
        
# Begin Script
if __name__ == '__main__':
    main()