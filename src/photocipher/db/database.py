###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################


import sqlite3 as sql
from paths import AppPathsManager
from queries import (
    TABLE_CREATION_QUERY,
    ENTRY_INSERTION_QUERY,
    ENTRY_RETRIEVAL_QUERY,
    ENTRY_DELETION_QUERY
)


class DB:

    def __init__(self, db_path: str) -> None:
        self.db_path: str = db_path

        # init DB, commit, && close connection
        with sql.connect(self.db_path) as db_connect:
            self.db_cursor: sql.Cursor = db_connect.cursor()

            # create table
            self.db_cursor.execute(TABLE_CREATION_QUERY)
            db_connect.commit()


    def insert(self) -> bool:
        pass


    def retrieve(self) -> bool:
        pass


    def delete(self) -> bool:
        pass



# export a general interface

db: DB = DB(AppPathsManager.get_db_path())

# eosc