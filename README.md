# PasswdGen
A password Generator in python


## Introduction
This is a password generation tool, useful to generate different passwords with custom pattern and length 


## Instalation

``` $ git clone https://github.com/Leooliveoi/PasswdGen/.git ```

``` $ python3 passwdgen.py ```

## Usage

This tool uses different arguments to generate passwords.


### Help

``` $ python3 passwdgen.py -h ```

### Version

``` $ python3 passwdgen.py -v ```


### Password length

+ Use **-l <int>** or **--length <int>** to declare the password length.

Example to generate a password with 5 characters:

``` $ python3 passwdgen.py -l 5 -L 1 ```

This is a mandatory argument.


### Password Complexity Level

Use **-L {1-4}** or **--level {1-4}** to declare the password complexity level.

This tool support 4 complexity levels.

1 = Only Numbers

2 = Numbers and lowercase characters

3 = Numbers, lower and uppercase characters

4 = Numbers, lowercase, uppercase and special characters

All the supported characters are: **"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_={}|[]\/?.>,<;:"**

Example to generate a strong password with 5 characters:

``` $ python3 passwdgen.py -l 5 -L 4 ```

This argument is mandatory.


### File Output

Use **-o** or **--output** to save the generated passwords in a file.

Example to save the generated password in a file named mypassword.txt:

``` $ python3 passwdgen.py -l 10 -L 4 -o mypassword.txt ```


### Password Quantity

Use **-q** **--quantity** to define the quantity of generated passwords.

Example to generate 10 strong passwords with 10 characters:

``` $ python3 passwdgen.py -l 10 -L 4 -q 10 ```


### Miscelaneous

Use **--no-banner** to hide the welcome banner.

Use **-s** or **--silent** to hide any terminal output.

 


