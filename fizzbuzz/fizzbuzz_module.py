def fizzbuzz(number):

    to_return = ""
    if number % 3 == 0:
        to_return += "Fizz"
    if number % 5 == 0:
        to_return += "Buzz"
    if not to_return:
        to_return = number
    return to_return


def main():
    num = ""
    for i in range(1, 101):
        num = fizzbuzz(i)
        print(num)
    return

if __name__ == '__main__':
    main()
