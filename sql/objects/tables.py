"""
A table generator

@author Andrew Evans
"""

import psycopg2


class Table:

    def __init__(self):
        """
        Constructor
        """
        self.__schema = None
        self.__table = None
        self.__fields = None

    @property
    def schema(self):
        """
        Get the schema

        :return:    The schema name
        """
        return self.__schema

    @schema.setter
    def schema(self, schema):
        """
        Set the schema name

        :param schema:  The schema name
        """
        self.__schema = schema

    @property
    def table(self):
        """
        Get the table name

        :return:    The table name
        """
        return self.__table

    @table.setter
    def table(self, table):
        """
        Set the table name

        :param table:   The table name
        """
        self.__table = table

    @property
    def fields(self):
        """
        Get the fields

        :return:    A fields object
        """
        return self.__fields

    @fields.setter
    def fields(self, fields):
        """
        Set the fields

        :param fields:  A fields object
        """
        self.__fields = fields
