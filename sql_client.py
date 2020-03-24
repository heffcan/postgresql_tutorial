"""
To connect to the suppliers database, use the connect() function of the
psycopg2 module

The connect() function create a new database session and returns a new instance
of the connection class.

With a connection create a cursor to execute SQL statements. Terminate transaction with commit() or rollback()
"""
import psycopg2


conn = psycopg2.connect("dbname=suppliers user=postgres password=postgres")

