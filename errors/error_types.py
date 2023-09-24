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
