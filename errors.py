class Error(Exception):
    def __init__(self, error_type, error_message):
        self.error_type = f"Error::{error_type}"
        self.error_message = error_message
        print(self)
        exit()
    
    def __str__(self):
        return f'{self.error_type} -> {self.error_message}'

class EvaluationNotPossible(Error):
    def __init__(self, error_type, error_message):
        self.error_type = f"EvaluationNotPossible::{error_type}"
        self.error_message = error_message
        super().__init__(self.error_type, self.error_message)

class InvalidSyntax(Error):
    def __init__(self, error_type, error_message):
        self.error_type = f"InvalidSyntax::{error_type}"
        self.error_message = error_message
        super().__init__(self.error_type, self.error_message)

class MissingValue(EvaluationNotPossible):
    def __init__(self, idx):
        self.error_type = "MissingValue"
        self.error_message = f"Missing value at index {idx}"
        super().__init__(self.error_type, self.error_message)

class MissingOperand(EvaluationNotPossible):
    def __init__(self):
        self.error_type = "MissingOperand"
        self.error_message = "Missing operand in the expression"
        super().__init__(self.error_type, self.error_message)

class InvalidOperand(EvaluationNotPossible):
    def __init__(self, idx):
        self.error_type = "InvalidOperand"
        self.error_message = f"Invalid operand at index {idx}"
        super().__init__(self.error_type, self.error_message)

class InvalidValue(EvaluationNotPossible):
    def __init__(self, v):
        self.error_type = "InvalidValue"
        self.error_message = f"Invalid value : {v}"
        super().__init__(self.error_type, self.error_message)

class InvalidCharacter(InvalidSyntax):
    def __init__(self, ch):
        self.error_type = "InvalidCharacter"
        self.error_message = f"Invalid character : {ch}"
        super().__init__(self.error_type, self.error_message)

class EvaluationEndingByANumber(InvalidSyntax):
    def __init__(self):
        self.error_type = "EvaluationEndingByANumber"
        self.error_message = f"The evaluation ends by a number"
        super().__init__(self.error_type, self.error_message)