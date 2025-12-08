###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################


import sqlite3 as sql
from paths import AppPathsManager
from const import DB_FILE_NAME
from queries import (
    TABLE_CREATION_QUERY,
    TABLE_EXISTS_QUERY,
    ENTRY_INSERTION_QUERY,
    ENTRY_RETRIEVAL_QUERY,
    ENTRY_DELETION_QUERY
)
from errors import *


class DB:

    def __init__(self, db_name, db_path: str) -> None:
        self.db_path: str = db_path
        self.db_name: str = db_name

        # init DB, commit, && close connection
        with sql.connect(self.db_path) as db_connect:
            self.db_cursor: sql.Cursor = db_connect.cursor()

            # create table
            self.db_cursor.execute(TABLE_CREATION_QUERY)
            db_connect.commit()


    def _check_table_exists(self, cursor: sql.Cursor) -> bool:
        cursor.execute(
            TABLE_EXISTS_QUERY,
            (DB_FILE_NAME,)
        )
        return (cursor.fetchone()[0] > 0)


    def insert(self, entry: tuple[str, ...]) -> bool:
        with sql.connect(self.db_path) as conn:
            self.cursor: sql.Cursor = conn.cursor()

            if not self._check_table_exists(self.cursor):
                self.cursor.execute(
                    TABLE_CREATION_QUERY
                )
            try:
                self.cursor.execute(
                    ENTRY_INSERTION_QUERY,
                    entry
                )
            except: # most likely a duplicate entry scenario
                raise ENTRY_EXISTS("Entry exists in the database")
            conn.commit()
        return True


    def retrieve(self, eci_hash: str) -> tuple[str, ...] | None:
        with sql.connect(self.db_path) as conn:
            self.cursor: sql.Cursor = conn.cursor()

            if not self._check_table_exists(self.cursor):
                self.cursor.execute(
                    TABLE_CREATION_QUERY
                )
                raise ENTRY_NOT_FOUND("Table does not exists")
            
            self.cursor.execute(
                ENTRY_RETRIEVAL_QUERY,
                (eci_hash,)
            )
            output: tuple[str, ...] | None = self.cursor.fetchone()
            if not output:
                raise ENTRY_NOT_FOUND("Entry does not exists")
        return output


    def delete(self) -> bool:
        pass



# export a general interface

db: DB = DB(
    DB_FILE_NAME,
    AppPathsManager.get_db_path()
)

# eosc