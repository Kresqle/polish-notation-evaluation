from error_types import EvaluationNotPossible

class MissingValue(EvaluationNotPossible):
    def __init__(self, idx):
        self.error_type = "MissingValue"
        self.error_message = f"Missing value at index {idx}"
        super().__init__(self.error_type, self.error_message)

class MissingOperand(EvaluationNotPossible):
    def __init__(self):
        self.error_type = "MissingOperand"
        self.error_message ) "Missing operand in the expression"
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
        super().__init__(self.error_type, self.error_message
