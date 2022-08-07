


class X(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class Y(X):
    def __init__(self, s_msg) -> None:
        super().__init__(s_msg)