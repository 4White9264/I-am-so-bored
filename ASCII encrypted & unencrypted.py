# this program is aiming to making translation between normal language

def encrypted(string):
    result = ''
    for alphbet in string:
        encrypt = ord(alphbet)
        result += str(encrypt)
        result += " "
    return result


def unencrypted(ascii_code):
    result = ''
    spliting = ascii_code.split(" ")
    for ascii in spliting:

        if ascii != " ":
            unencrypt = chr(int(ascii))
            result += str(unencrypt)
    return result


def main():
    print("If you trying to translate something to ascii code, please input 1")
    print("If you trying to translate ascii code to something, please input 2")
    inputing = input("Your input is: ")
    while inputing != "1" and inputing != "2":
        print("undefined error, please retype again")
        print("If you trying to translate something to ascii code, please input 1")
        print("If you trying to translate ascii code to something, please input 2")
        inputing = input("Your input is: ")

    if inputing == "1":
        print("Please input what you need to translate")
        inputing = input("Your input is: ")
        need_unencrypted = inputing
        print(" ")
        print("=====Encrypted result=====")
        print(encrypted(need_unencrypted))
        print(" ")
        print("The program is finished")


    else:
        print("Please input what you need to translate")
        inputing = input("Your input is: ")
        need_unencrypted = inputing
        print(" ")
        print("=====Unencrypted result=====")
        print(unencrypted(need_unencrypted))
        print(" ")
        print("The program is finished")


main()
