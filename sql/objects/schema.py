"""
Schema object

@author Andrew Evans
"""

from sql.query import create_schema_query_generator


class Schema:
    """
    Schema object
    """

    def __init__(self, name, authorization=None, if_not_exists=False):
        """
        Schema related object

        :param name:    Name of the schema
        :param authorization:   Authorized user
        :param if_not_exists:   Whether to ignore if the schema exists
        """
        self.__name = name
        self.__authorization = authorization
        self.__if_not_exists = if_not_exists

    @property
    def if_not_exists(self):
        """
        Get whether the schema may not exists

        :return:    Whether to ignore if the query exists
        """
        return self.__if_not_exists

    @if_not_exists.setter
    def if_not_exists(self, exists):
        """
        Set whether to ignore if the schema exists

        :param exists: Whether to ignore if the schema exists
        """
        self.__if_not_exists = exists

    @property
    def name(self):
        """
        Get the schema name

        :return:    The schema name
        """
        return self.__name

    @name.setter
    def name(self, inname):
        """
        Set the name of the schema

        :param inname:  The schema name
        """
        self.__name = inname

    @property
    def authorization(self):
        """
        Get the name of the authorized user(s)

        :return:     The authorized user(s)
        """
        return self.__authorization

    @authorization.setter
    def authorization(self, authorization):
        """
        Set the authorized user(s)

        :param authorization:    authorized user(s)
        """
        self.__authorization = authorization

    def __str__(self):
        """
        Turn this object into a create statement

        :return:    Relevant create statement
        """
        return create_schema_query_generator.generate_query(self)