###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################


from platformdirs import user_data_dir
from pathlib import Path
from const import (
    APP_NAME,
    APP_DEVELOPER,
    DB_FILE_NAME,
    DB_DIR_NAME
)


class AppPathsManager:
    
    def __init__(
        self,
        app_name: str,
        app_dev: str,
        db_name: str,
        db_dir: str
    ) -> None:
        
        self.app_name: str = app_name
        self.app_dev: str = app_dev

        self.user_data_dir: Path = Path(
            user_data_dir(
                self.app_name, 
                self.app_dev
            )
        )
        
        self.db_name: str = db_name
        self.db_dir: Path = self.user_data_dir / db_dir

        self.db_full_path: Path = self.db_dir / self.db_name

        # create database directory
        if not self.db_dir.exists():
            Path.mkdir(self.db_dir, parents=True)
        

    def get_db_path(self) -> str:
        return str(self.db_full_path)



# export a general interface

app_paths: AppPathsManager = AppPathsManager(
    APP_NAME,
    APP_DEVELOPER,
    DB_FILE_NAME,
    DB_DIR_NAME
)

# eosc