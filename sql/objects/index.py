"""
An index

@author Andrew Evans
"""


class Index:
    """
    Index object
    """

    def __init__(self, name, table, unique=False, concurrent=False, order=None):
        """
        Constructor
        """
        self.__name = name
        self.__table = table
        self.__unique = unique
        self.__concurrent = concurrent
        self.__order = order

    @property
    def order(self):
        """
        Get the order which may be none (unused)

        :return:    The order
        """
        return self.__order

    @order.setter
    def order(self, inorder):
        """
        Set the order of the index ASC, DESC

        :param inorder: The order
        """
        self.__order = inorder

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
