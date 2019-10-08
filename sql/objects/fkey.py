"""
Foreign key index

@author Andrew Evans
"""


class FKIndex:
    """
    Foreign key index object
    """

    def __init__(self, ref_table, foreign_table_field):
        """
        Constructor
        """
        self.__foreign_table_field = foreign_table_field
        self.__ref_table = ref_table

    @property
    def foreign_table_field(self):
        """
        Get the foreign table fields

        :return:    The foreign table fields list
        """
        return self.__foreign_table_fields

    @foreign_table_field.setter
    def foreign_table_field(self, field):
        """
        Set the foreign table field

        :param field:  The foreign table fields list
        """
        self.__foreign_table_field = field

    @property
    def ref_table(self):
        """
        Get the reference table

        :return:    The reference table name
        """
        return self.__ref_table

    @ref_table.setter
    def ref_table(self, table):
        """
        SEt the reference table

        :param table:   The table name
        """
        self.__ref_table = table

    def __str__(self):
        """
        Return a field value
        :return:    The useable field value
        """
        if self.__ref_table is not None and self.__foreign_table_field is not None:
            val = "REFERENCES {}".format(self.ref_table.trim())
            val = "{}({})".format(val, self.foreign_table_field)
            return val
        else:
            raise ValueError("Reference table and field cannto be null")
