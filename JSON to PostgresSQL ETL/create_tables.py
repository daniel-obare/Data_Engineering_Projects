import psycopg2
from db_conn import get_database_connection
from queries import create_table_queries, drop_table_queries


def create_database():
    """
    - Creates and connects to the musicplaylist
    - Returns the connection and cursor to musicplaylist
    """
    # Connect to the default database
    default_conn = get_database_connection()
    default_conn.set_session(autocommit=True)
    default_cur = default_conn.cursor()
    
    # Create musicapp_db database with UTF8 encoding
    default_cur.execute("DROP DATABASE IF EXISTS musicplaylist")
    default_cur.execute("CREATE DATABASE musicplaylist WITH ENCODING 'utf8' TEMPLATE template0")

    # Close connection to default database
    default_conn.close()    
    
    # Connect to musicapp_db database
    conn = get_database_connection(database_name="musicplaylist")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the musicplaylist database. 
    
    - Establishes connection with the musicplaylist database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
