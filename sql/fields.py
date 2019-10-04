"""
Table Fields

@author Andrew Evans
"""


class TableField:
    """
    A non-foreign key field
    """

    def __init__(
            self, name, type, primary_key=False, default_val=None, not_null=True, foreign_key=None):
        """
        Constructor

        :param name:    The name of the field
        :param type:    The field type
        :param primary_key: Whether
        :param default_val: The default value
        :param not_null: Whether the field can be null or not
        :param foreign_key: Foreign key information for field
        """
        self.__name = name
        self.__primary_key = primary_key
        self.__not_null = not_null
        self.__foreign_key = foreign_key
        self.__type = type
        self.__default_val = default_val

    @property
    def name(self):
        """
        Get the name of the field

        :return: The field name
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Set the name of the field

        :param name:    The name of the field
        """
        self.__name = name

    @property
    def type(self):
        """
        Get the variable type

        :return:     The variable type
        """
        return self.__type

    @type.setter
    def type(self, type_name):
        """
        Set the variable type

        :param type_name:   The variable type name
        """
        self.__type = type_name

    @property
    def primary_key(self):
        """
        Get the primary key name
        :return:    Name of the primary key
        """
        return self.__primary_key

    @primary_key.setter
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

    @not_null.setter
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

    @foreign_key.setter
    def foreign_key(self, fkey):
        """
        Set the foreign key object associated with the field

        :param fkey:    The foriegn key object
        """
        self.__foreign_key = fkey

    @property
    def default_val(self):
        """
        Get the default value

        :return:    default value
        """
        return self.__default_val

    @default_val.setter
    def default_val(self, default_val):
        """
        Set the default value

        :param default_val: The default value
        """
        self.__default_val = default_val

    def __str__(self):
        """
        Get the string representation
        :return:    String representation
        """
        val = "{} {}".format(self.name, self.type)
        if self.foreign_key:
            val = "{} {}".format(val, str(self.foreign_key))
        if self.default_val:
            val = "{} DEFAULT {}".format(val, str(self.default_val))
        if self.not_null:
            val = "{} {}".format(val, "NOT NULL")
        return val


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

    @fields.setter
    def fields(self, fields):
        """
        Set the fields associated with this object

        :param fields: Fields for the object
        """
        if fields:
            self.__fields = fields

    def add_field(self, field):
        """
        The field to add

        :param field:   The field object
        """
        self.fields.append(field)

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

    def __str__(self):
        """
        Create a query from the fields

        :return: The query created from teh object
        """
        if self.fields:
            q = None
            for field in self.fields:
                if q:
                    q = "{}, {}".format(q, str(field))
                else:
                    q = "({}".format(str(field))
            pkeys = [x.name for x in self.fields if x.primary_key is True]
            if pkeys and len(pkeys) > 0:
                pkstr = ','.join(pkeys)
                q = "{}, PRIMARY KEY({})".format(q, pkstr)
            q = "{})".format(q)
            return q
        else:
            raise ValueError("Fields cannot be null")
