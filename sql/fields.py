"""
Table Fields

@author Andrew Evans
"""


class TableField:
    """
    A non-foreign key field
    """

    def __init__(self, name, type, primary_key=False, not_null=True, foreign_key=None):
        """
        Constructor

        :param name:    The name of the field
        :param type:    The field type
        :param primary_key: Whether
        :param not_null: Whether the field can be null or not
        :param foreign_key: Foreign key information for field
        """
        self.__name = name
        self.__primary_key = primary_key
        self.__not_null = not_null
        self.__foreign_key = foreign_key

    @property
    def name(self):
        """
        Get the name of the field
        :return: The field name
        """
        return self.__name

    @property.setter
    def name(self, name):
        """
        Set the name of the field

        :param name:    The name of the field
        """
        self.__name = name

    @property
    def primary_key(self):
        """
        Get the primary key name
        :return:    Name of the primary key
        """
        return self.__primary_key

    @property.setter
    def primary_key(self, primary_key):
        """
        Set the primary key

        :param primary_key: The primary key name
        """
        self.__primary_key = primary_key

    @property
    def not_null(self):
        """
        Whether this field is allowed to be null

        :return:    Whether or not the field is null
        """
        return self.__not_null

    @property.setter
    def not_null(self, not_null):
        """
        Set whether this field may be null

        :param not_null:    Whether or not the field may be null
        """
        self.__not_null = not_null

    @property
    def foreign_key(self):
        """
        Get the foriegn key object associated with this field
        :return:    The foriegn key object associated with the field
        """
        return self.__foreign_key

    @property.setter
    def foreign_key(self, fkey):
        """
        Set the foreign key object associated with the field

        :param fkey:    The foriegn key object
        """
        self.__foreign_key = fkey


class Fields:
    """
    A field object
    """

    def __init__(self):
        """
        Constructor
        """
        self.__iter = 0
        self.__fields = []

    @property
    def fields(self):
        """
        Get the fields object list

        :return:    List of field objects associated with this class
        """
        return self.__fields

    @property.setter
    def fields(self, fields):
        """
        Set the fields associated with this object

        :param fields: Fields for the object
        """
        if fields:
            self.__fields = fields

    def __iter__(self):
        """
        Turn Field
        :return:
        """
        self.__iter = 0
        return self

    def __next__(self):
        """
        Get the next field object if available

        :return:    The next field object
        """
        if self.__iter < len(self.__fields):
            nval = self.__fields[self.__iter]
            self.__iter += 1
            return nval
        else:
            raise StopIteration
