###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################


class ENTRY_EXISTS(Exception):
    
    def __init__(self, message: str) -> None:
        self.message: str = "[REASON] " + message
        super().__init__(self.message)


class ENTRY_NOT_FOUND(Exception):
    
    def __init__(self, message: str) -> None:
        self.message: str = "[REASON] " + message
        super().__init__(self.message)


class CANNOT_DELETE_ENTRY(Exception):

    def __init__(self, message: str) -> None:
        self.message: str = "[REASON] " + message
        super().__init__(self.message)



# export public ones

__all__: list[str] = [
    "ENTRY_EXISTS",
    "ENTRY_NOT_FOUND",
    "CANNOT_DELETE_ENTRY"
]

# eosc