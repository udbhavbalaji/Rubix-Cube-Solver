class InvalidOperationError(Exception):
    def __init__(self, msg: str) -> None:
        # YOUR CODE HERE
        super().__init__(msg)


class CubeIntegrityError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class ShuffleError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class InvalidEdgePieceError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
