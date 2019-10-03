"""
A table generator

@author Andrew Evans
"""

import psycopg2


class TableGenerator:

    def __init__(self, conn):
        """
        Constructor

        :param conn:    The connection
        """
        self.__conn = conn

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
        if self.__conn is not None:
            self.__conn.close
            self.__conn = None

    def create_table(self, table_object):
        """
        Create a table from a table object

        :param table_object: Object containing table information
        """
        schema = table_object.schema
        table = table_object.table
        fields = table_object.fields