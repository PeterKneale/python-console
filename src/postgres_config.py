import os

class PostgresConfig:
    def __init__(self):
        self.db_host = os.environ.get('DB_HOST',"postgres")
        self.db_database = os.environ.get('DB_DATABASE',"postgres")
        self.db_username = os.environ.get('DB_USERNAME',"postgres")
        self.db_password = os.environ.get('DB_PASSWORD',"postgres")

    def get_connection_string(self):
        if not all([self.db_host, self.db_database, self.db_username, self.db_password]):
            raise ValueError("One or more environment variables are missing.")

        return f"postgresql://{self.db_username}:{self.db_password}@{self.db_host}/{self.db_database}"
