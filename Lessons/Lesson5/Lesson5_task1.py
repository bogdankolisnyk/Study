import string
import keyword

var = input("Enter variable: ")

invalid_chars = string.punctuation.replace("_", "")  # Знаки пунктуації без "_"

if not var:
    print("Wrong variable: input cannot be empty.")
elif var in keyword.kwlist:
    print("Wrong variable: it is a Python keyword.")
elif var[0].isdigit():
    print("Wrong variable: it starts with a digit.")
elif any(char.isspace() or char in invalid_chars for char in var):
    print("Wrong variable: it contains spaces or invalid punctuation.")
elif var.count("_") > 1:
    print("Wrong variable: it contains more than one underscore.")
elif any(char.isupper() for char in var):
    print("Wrong variable: it contains uppercase letters.")
else:
    print(f"'{var}' is a valid variable name.")