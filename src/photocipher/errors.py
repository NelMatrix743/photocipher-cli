###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################


class ENTRY_EXISTS(Exception):
    
    def __init__(self) -> None:
        self.message: str = "[ERROR] Entry exists in the database"
        super().__init__(self.message)


class ENTRY_NOT_FOUND(Exception):
    
    def __init__(self) -> None:
        self.message: str = "[ERROR] Entry could not be retrieved"
        super().__init__(self.message)



# export public ones

__all__: list[str] = ["ENTRY_EXISTS", "ENTRY_NOT_FOUND"]

# eosc