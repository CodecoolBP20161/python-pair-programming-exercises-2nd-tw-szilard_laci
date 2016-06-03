def passwordgen(passwordlength=8):
    from random import randrange
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()?"
    chars = lowercase + uppercase + numbers + symbols
    while True:
        pw = ""
        lowc_bool = False
        upc_bool = False
        numbool = False
        symbool = False
        for i in range(passwordlength):
            char_to_insert = chars[randrange(1, len(chars))]
            pw = pw[:len(pw)] + char_to_insert
            if char_to_insert in lowercase:
                lowc_bool = True
            if char_to_insert in uppercase:
                upc_bool = True
            if char_to_insert in numbers:
                numbool = True
            if char_to_insert in symbols:
                symbool = True
        if lowc_bool is True and upc_bool is True and numbool is True and symbool is True:
            return pw


def main():
    while True:
        try:
            length = input("How many characters should your password have? (min 8) ")
            if int(length) > 7:
                break
            print("Your password length can't be less than 8!")

        except ValueError:
            print("Please enter a number!")
    print(passwordgen(int(length)))


if __name__ == '__main__':
    main()
