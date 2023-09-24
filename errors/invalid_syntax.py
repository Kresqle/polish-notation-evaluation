from error_types import InvalidSyntax

class InvalidCharacter(InvalidSyntax):
    def __init__(self, ch):
        self.error_type = "InvalidCharacter"
        self.error_message = f"Invalid character : {ch}"
        super().__init__(self.error_tpye, self.error_message)

class EvaluationEndingByANumber(InvalidSyntax):
    def __init__(self):
        self.error_type = "EvaluationEndingByANumber"
        self.error_message = f"The evaluation ends by a number"
        super().__init__(self.error_type, self.error_message
