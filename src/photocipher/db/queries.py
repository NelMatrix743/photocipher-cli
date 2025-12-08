###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################

from const import DB_TABLE_NAME


# CRD -> Create, Read, Delete (no Update action)

table_creation_query: str = f"""
    CREATE TABLE IF NOT EXISTS {DB_TABLE_NAME} (
        eci_entry_id text NOT NULL PRIMARY KEY,
        cryptographic_key text NOT NULL,
        img_filename text NOT NULL,
        en_img_filename text NOT NULL,
        date text NOT NULL,
        time text NOT NULL
    );
"""


table_entry_insert_query: str = f"""
    INSERT INTO {DB_TABLE_NAME}(
        eci_entry_id,
        cryptographic_key, 
        img_filename, 
        en_img_filename, 
        date, 
        time          
        )
    VALUES(?, ?, ?, ?, ?, ?);
"""


table_entry_retrieval_query: str = f"""
    SELECT * FROM {DB_TABLE_NAME} WHERE eci_entry_id = ?;
"""


table_entry_delete_entry: str = f"""
    DELETE FROM {DB_TABLE_NAME} WHERE eci_entry_id = ?;
"""

# eosc