###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################

from const import DB_TABLE_NAME


# CRD -> Create, Read, Delete (no Update action)

TABLE_CREATION_QUERY: str = f"""
    CREATE TABLE IF NOT EXISTS {DB_TABLE_NAME} (
        eci_hash text NOT NULL PRIMARY KEY,
        cryptographic_key text NOT NULL,
        img_filename text NOT NULL,
        en_img_filename text NOT NULL,
        date text NOT NULL,
        time text NOT NULL
    );
"""


TABLE_EXISTS_QUERY: str = f"""
    SELECT count(*) FROM sqlite_master
    WHERE type='table' AND name={DB_TABLE_NAME};
"""

ENTRY_INSERTION_QUERY: str = f"""
    INSERT INTO {DB_TABLE_NAME} (
        eci_hash,
        cryptographic_key, 
        img_filename, 
        en_img_filename, 
        date, 
        time          
    ) VALUES(?, ?, ?, ?, ?, ?);
"""


ENTRY_RETRIEVAL_QUERY: str = f"""
    SELECT * FROM {DB_TABLE_NAME} WHERE eci_hash = ?;
"""


ENTRY_DELETION_QUERY: str = f"""
    DELETE FROM {DB_TABLE_NAME} WHERE eci_hash = ?;
"""

# eosc