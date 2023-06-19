import argparse

import psycopg2
from src.postgres_config import PostgresConfig
from src.calculator import add_numbers

if __name__ == '__main__':

    config = PostgresConfig()
    connection_string = config.get_connection_string()
    connection = psycopg2.connect(connection_string)
    try:
        print(f"Connecting to version: {connection_string}")
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()[0]
        print(f"Database version: {db_version}")
    except (psycopg2.Error, Exception) as error:
        print(f"Error connecting to the database: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            