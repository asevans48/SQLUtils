"""
Foreign key index

@author Andrew Evans
"""


class FKIndex:
    """
    Foreign key index object
    """

    def __init__(self):
        """
        Constructor
        """
        self.__foreign_table_fields
        self.__ref_Table

    @property
    def foreign_table_fields(self):
        """
        Get the foreign table fields

        :return:    The foreign table fields list
        """
        return self.__foreign_table_fields

    @property.setter
    def foreign_table_fields(self, fields):
        """
        Set the foreign table fields

        :param fields:  The foreign table fields list
        """
        self.__foreign_table_fields = fields

    @property
    def ref_table(self):
        """
        Get the reference table

        :return:    The reference table name
        """
        return self.__ref_table

    @property.setter
    def ref_table(self, table):
        """
        SEt the reference table

        :param table:   The table name
        """
        self.__ref_table = table