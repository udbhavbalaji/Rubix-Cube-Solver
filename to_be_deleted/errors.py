

class ArgumentTypeError(Exception):
    
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)
        
        

class IncorrectTypeError(Exception):
    
    def __init__(self, message : str) -> None:
        super().__init__(message)