from os import system
from colorama import Fore

system("Title Temperature converter")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)


def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)


def wrong_number():
    print(Fore.RED + "number not recognized please start over")
    main()


def one():
    celsius = (input("how many degrees delicious do you want to convert from?\n"))

    try:
        celsius = float(celsius)
        print(celsius_to_fahrenheit(celsius), "degrees fahrenheit")
    except ValueError:
        wrong_number()


def two():
    fahernheit = (input("How many degrees fahrenheit do you want to convert from?\n"))

    try:
        fahernheit = float(fahernheit)
        print(fahrenheit_to_celsius(fahernheit), "degrees celcius")
    except ValueError:
        wrong_number()


def three():
    kelvin = (input("how many degrees kelvin do you want to convert from?\n"))

    try:
        kelvin = float(kelvin)
        print(kelvin_to_celsius(kelvin), "degrees celcius")
    except ValueError:
        wrong_number()


def four():
    kelvin2 = (input("how many degrees kelvin do you want to convert from?\n"))

    try:
        kelvin2 = float(kelvin2)
        print(kelvin_to_fahrenheit(kelvin2), "degrees fahrenheit")
    except ValueError:
        wrong_number()


def five():
    celsius = (input("how many degrees celcius do you want to convert from?\n"))

    try:
        celsius = float(celsius)
        print(celsius_to_kelvin(celsius), "degrees kelvin")
    except ValueError:
        wrong_number()


def six():
    fahernheit2 = (input("how many degrees fahrenheit do you want to convert from?\n"))

    try:
        fahernheit2 = float(fahernheit2)
        print(fahrenheit_to_kelvin(fahernheit2), "degrees kelvin")
    except ValueError:
        wrong_number()


def none():
    print(Fore.RED + "please type a number 1-6 or exit to exit")
    main()


def main():
    number = 9
    print(Fore.WHITE + "\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n" +
          "3. Kelvin to Celsius\n4. Kelvin to Fahrenheit\n5. Celsius to Kelvin\n" +
          "6. Fahrenheit to Kelvin\n0. to exit")
    while number != 0:
        try:
            number = int(input("Enter the number of your choice: "))
            if number == 1:
                one()
            elif number == 2:
                two()
            elif number == 3:
                three()
            elif number == 4:
                four()
            elif number == 5:
                five()
            elif number == 6:
                six()
            elif number == 0:
                print('exiting...')
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print(Fore.RED, "\nInvalid choice. Please enter a number 1-6 or 0 to exit")


if __name__ == "__main__":
    print("run in main file")
