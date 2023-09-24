class Token:
    NUMS = "0123456789",
    OPERANDS = {
            "+": lambda x, y : x + y,
            "-": lambda x, y : x - y,
            "*": lambda x, y : x * y,
            "/": lambda x, y : x / y,
            "^": lambda x, y : x ** y,
            "%": lambda x, y : x % y
    }

class NotationType:
    POSTFIX = "postfix"
