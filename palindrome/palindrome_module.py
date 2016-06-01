def palindrome(string):
    string = string.replace(" ", "")
    string = string.lower()
    if string == string[::-1]:
        return True
    else:
        return False


def main():
    text = input("Enter text: ")
    if palindrome(text):
        print(text, "IS a palindrome")
    else:
        print(text, "is NOT a palindrome")



if __name__ == '__main__':
    main()
