###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################


import sqlite3 as sql
from paths import AppPathsManager
from const import DB_TABLE_NAME
from queries import (
    TABLE_CREATION_QUERY,
    ENTRY_INSERTION_QUERY,
    ENTRY_RETRIEVAL_QUERY,
    ENTRY_DELETION_QUERY
)
from errors import *


class DB:

    def __init__(self, tb_name, db_path: str) -> None:
        self.db_path: str = db_path
        self.table_name: str = tb_name

        # init DB, commit, && close connection
        with sql.connect(self.db_path) as db_connect:
            cursor: sql.Cursor = db_connect.cursor()

            # create table
            cursor.execute(TABLE_CREATION_QUERY)
            db_connect.commit()


    def insert(self, entry: tuple[str, ...]) -> bool:
        with sql.connect(self.db_path) as conn:
            cursor: sql.Cursor = conn.cursor()

            try:
                cursor.execute(
                    ENTRY_INSERTION_QUERY,
                    entry
                )
                conn.commit()
            except sql.IntegrityError: # likely a duplicate entry
                raise ENTRY_EXISTS("Entry exists in the database")
        return True


    def retrieve(self, eci_hash: str) -> tuple[str, ...] | None:
        with sql.connect(self.db_path) as conn:
            cursor: sql.Cursor = conn.cursor()

            cursor.execute(
                ENTRY_RETRIEVAL_QUERY,
                (eci_hash,)
            )
            output: tuple[str, ...] | None = cursor.fetchone()
            if not output:
                raise ENTRY_NOT_FOUND("Entry does not exist")
        return output


    def delete(self, eci_hash: str) -> bool:
        with sql.connect(self.db_path) as conn:
            cursor: sql.Cursor = conn.cursor()

            cursor.execute(
                ENTRY_DELETION_QUERY,
                (eci_hash,)
            )
            conn.commit()
            if not cursor.rowcount: # (count == 0)
                raise CANNOT_DELETE_ENTRY("Entry does not exist")
        return True



# export a general interface

db: DB = DB(
    DB_TABLE_NAME,
    AppPathsManager.get_db_path()
)

# eosc