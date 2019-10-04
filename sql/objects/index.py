"""
An index

@author Andrew Evans
"""

from sql.query import index_query_generator


class Index:
    """
    Index object
    """

    def __init__(
            self,
            name,
            table,
            columns,
            if_not_exists=False,
            schema=None,
            using=None,
            unique=False,
            concurrent=False,
            use_with=None,
            tablespace=None,
            condition=None):
        """
        Constructor
        """
        self.__if_not_exists = if_not_exists
        self.__name = name
        self.__table = table
        self.__schema = schema
        self.__unique = unique
        self.__concurrent = concurrent
        self.__columns = columns
        self.__using = using
        self.__use_with = use_with
        self.__tablespace = tablespace
        self.__condition = condition

    @property
    def if_not_exists(self):
        """
        Get whether the index must exist or not

        :return:    Whether to fail if index exists or not
        """
        return self.__if_not_exists

    @if_not_exists.setter
    def if_not_exists(self, exists):
        """
        Set whether to ignore if exists

        :param exists:  ignore if exists
        """
        self.__if_not_exists = exists

    @property
    def table(self):
        """
        Get the table name property

        :return:    The table name
        """
        return self.__table

    @table.setter
    def table(self, intable):
        """
        Set the table name

        :param intable: The table name
        """
        self.__table = intable

    @property
    def schema(self):
        """
        Get the name of the schema

        :return:    The schema name
        """
        return self.__schema

    @schema.setter
    def schema(self, inschema):
        """
        Set the schema name
        :param inschema:    The schema
        """
        self.__schema = inschema

    @property
    def condition(self):
        """
        Get the condition

        :return:    Condition string
        """
        return self.__condition

    @condition.setter
    def condition(self, condition):
        """
        Set the condition

        :param condition:   The condition string
        """
        self.__condition = condition

    @property
    def tablespace(self):
        """
        The tablespace to use

        :return:    The tablespace name
        """
        return self.__tablespace

    @tablespace.setter
    def tablespace(self, tablespace):
        """
        Set the tablespace

        :param tablespace:  The tablespace name
        """
        self.__tablespace = tablespace

    @property
    def use_with(self):
        """
        Get methods to use with

        :return:    List of  parameters to use with
        """
        return self.__use_with

    @use_with.setter
    def use_with(self, use_with):
        """
        Set the use_with options
        """
        self.__use_with = use_with

    @use_with.setter
    def use_with(self, use_with):
        """
        Set
        :param use_with:
        :return:
        """

    @property
    def using(self):
        """
        Get the using method

        :return:    The using method
        """
        return self.__using

    @using.setter
    def using(self, using):
        """
        Set the method to use
        """
        self.__using = using

    @property
    def columns(self):
        """
        Get the relevant columns
        :return:    Column string list
        """
        return self.__columns

    @columns.setter
    def columns(self, columns):
        """
        Set the columns

        :param columns: The columns
        """
        self.__columns = columns

    @property
    def concurrent(self):
        """
        Whether the index is created concurrently

        :return: Whether the index is created concurrently
        """
        return self.__concurrent

    @concurrent.setter
    def concurrent(self, is_concurrent):
        """
        Set whether the index is concurrent

        :param is_concurrent:   Whether the index is concurrent
        """
        self.__concurrent = is_concurrent

    @property
    def unique(self):
        """
        Get whether the index is unique

        :return:    Whether the field is unique
        """
        return self.__unique

    @unique.setter
    def unique(self, is_unique):
        """
        Set whether the index is unique

        :param is_unique:   Whether the index is unique
        """
        self.__unique = is_unique

    @property
    def name(self):
        """
        Get the name

        :return:    Name of the index
        """
        return self.__name

    @name.setter
    def name(self, inname):
        """
        Set the name of the index

        :param inname:  The index name
        """
        self.__name = inname

    def __str__(self):
        """
        Convert the index to a create query
        :return:    A create query
        """
        return index_query_generator.generate_index_query(self)
