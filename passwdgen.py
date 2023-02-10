import random
import argparse
import datetime


def banner():
    print("""
    ███████████                                                █████   █████████                     
    ░░███░░░░░███                                              ░░███   ███░░░░░███                    
     ░███    ░███  ██████    █████   █████  █████ ███ █████  ███████  ███     ░░░   ██████  ████████  
     ░██████████  ░░░░░███  ███░░   ███░░  ░░███ ░███░░███  ███░░███ ░███          ███░░███░░███░░███ 
     ░███░░░░░░    ███████ ░░█████ ░░█████  ░███ ░███ ░███ ░███ ░███ ░███    █████░███████  ░███ ░███ 
     ░███         ███░░███  ░░░░███ ░░░░███ ░░███████████  ░███ ░███ ░░███  ░░███ ░███░░░   ░███ ░███ 
     █████       ░░████████ ██████  ██████   ░░████░████   ░░████████ ░░█████████ ░░██████  ████ █████
    ░░░░░         ░░░░░░░░ ░░░░░░  ░░░░░░     ░░░░ ░░░░     ░░░░░░░░   ░░░░░░░░░   ░░░░░░  ░░░░ ░░░░░ 
                                                                               Created by: Leonardo Oi
    """)


def generate_string(length, level):
    try:
        result = ""
        lowercase_alphabets = "0123456789"
        uppercase_alphabets = "0123456789"
        numbers = "0123456789"

        if level == 1:
            numbers = "0123456789"

        elif level == 2:
            lowercase_alphabets = "abcdefghijklmnopqrstuvwxyz"
            numbers = "0123456789"

        elif level == 3:
            lowercase_alphabets = "abcdefghijklmnopqrstuvwxyz"
            uppercase_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            numbers = "0123456789"

        elif level == 4:
            lowercase_alphabets = "abcdefghijklmnopqrstuvwxyz"
            uppercase_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            numbers = "0123456789!@#$%^&*()_={}|[]\/?.>,<;:"
        else:
            print("Error when parsing level")

        for i in range(length):

            sets = [lowercase_alphabets, uppercase_alphabets, numbers]

            if i % 4 == 0:
                result += random.choice(random.choice(sets[random.randint(0, 2)]))
            elif i % 4 == 1:
                result += random.choice(random.choice(sets[random.randint(0, 2)]))
            else:
                result += random.choice(random.choice(sets[random.randint(0, 2)]))
        return result
    except Exception as e:
        print(e)


def save_pass(password, filename, count):
    try:
        if filename is not None:
            with open(f"{filename}", "r+") as file:
                file.read()
                if count == 0:
                    date = datetime.datetime.now()
                    file.write(f"\n:==========> Created: {date}"+"\n")

                file.write(password + "\n")

            return count + 1

        else:
            pass

    except IOError:
        with open(f"{filename}", "w"):
            save_pass(password, filename, count)

    except Exception as e:
        print(e)


def arg_parser():
    try:
        arg = argparse.ArgumentParser(description="A password generator, can generate password with custom patterns "
                                                  "and custom length")
        arg.add_argument("-v", "--version", action="version", version="%(prog)s v0.01")

        arg.add_argument("-l", "--length", help="The password output length", type=int, required=True)
        arg.add_argument("-L", "--level",
                         help="The password complexity level: \n "
                              "(1 = numbers), \n "
                              "(2 = numbers and lowercase characters), \n"
                              "(3 = numbers, lowercase and uppercase characters), \n"
                              "(4 = numbers, lowercase, uppercase and special characters)",
                         type=int, required=True, choices=[1, 2, 3, 4])

        arg.add_argument("-q", "--quantity", help="The quantity of passwords to generate", type=int, required=False)
        arg.add_argument("-o", "--output", help="Save the generated password(s) in a file", type=str, required=False)
        arg.add_argument("--no-banner", help="Disable the Banner", choices=["true"], required=False)
        arg.add_argument("-s", "--silent", help="No terminal Outputs", choices=["true"], required=False)

        return arg.parse_args()

    except Exception as e:
        print(e)


def pass_parser(arguments):
    try:
        length = arguments.length
        level = arguments.level
        quantity = arguments.quantity
        filename = arguments.output
        count = 0
        if args.silent is None:
            print('Generated PASSWORDS:'.upper())

        if arguments.quantity is not None:
            for i in range(quantity):
                alphanumeric = generate_string(length, level)
                if args.silent is None:
                    print(f'{alphanumeric}')
                count = save_pass(alphanumeric, filename, count)
        else:
            alphanumeric = generate_string(length, level)
            if args.silent is None:
                print(f'{alphanumeric}')
            save_pass(alphanumeric, filename, count)

    except Exception as e:
        print(e)


if __name__ == "__main__":

    args = arg_parser()

    if args.silent is None:
        if args.no_banner is None:
            banner()

    pass_parser(args)
