"""
A table generator

@author Andrew Evans
"""

from sql import query_generator


class TableGenerator:

    def __init__(self, conn):
        """
        Constructor

        :param conn:    The connection
        """
        self.__conn = conn

    def close_cursor(self):
        """
        Close the cursor
        """
        if self.__conn is not None:
            self.__conn.close
            self.__conn = None

    def __enter__(self):
        """
        Turn this object into a closeable
        :return: self as a closeable
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the object and attached connection

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        """
        self.close_cursor()

    def create_table(self, table_object):
        """
        Create a table from a table object

        :param table_object: Object containing table information
        """
        qry = query_generator.generate_query(table_object)
        with self.__conn.cursor() as cursor:
            cursor.execute(qry)
