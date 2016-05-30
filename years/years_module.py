import time


def years(age):
    diff = 100 - age
    current_year = int((time.strftime("%Y")))
    return current_year + diff


def main():
    name = input("Whats your name? ")
    age = int(input("What's your age? "))

    print("You will be 100 years old in", years(age))

    return


if __name__ == '__main__':
    main()
