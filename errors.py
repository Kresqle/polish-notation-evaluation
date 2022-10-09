class Error(Exception):
    def __init__(self, error_type, error_message):
        self.error_type = f"Error::{error_type}"
        self.error_message = error_message
        super().__init__(f"{self.error_type} -> {self.error_message}")
    
    def __str__(self):
        return f'{self.error_type} -> {self.error_message}'

class EvaluationNotPossible(Error):
    def __init__(self, error_type, error_message):
        self.error_type = f"EvaluationNotPossible::{error_type}"
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