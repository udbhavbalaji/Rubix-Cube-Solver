

class InvalidOperationError(Exception):
    
    def __init__(self, msg: str) -> None:
        # YOUR CODE HERE
        super().__init__(msg)
    