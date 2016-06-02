def passwordgen():
    from random import randrange
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()?"
    chars = lowercase + uppercase + numbers + symbols
    let_it_go = False
    while let_it_go is False:
        pw = ""
        lowc_bool = False
        upc_bool = False
        numbool = False
        symbool = False
        for i in range(8):
            char_to_insert = chars[(randrange(1, len(chars)))]
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
    print(passwordgen())


if __name__ == '__main__':
    main()
