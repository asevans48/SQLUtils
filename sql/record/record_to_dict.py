"""
Convert a postgresql record to a dictionary

@author Andrew Evans
"""


class RecordToDict:
    """
    Record to dictionary converter
    """

    def __init__(self, mapping_list):
        """
        A mapping list of tuple indices to keys

        :param mapping_list:    The mapping list
        """
        self.__mapping_list = mapping_list

    def convert_record(self, record):
        """
        Convert a record to a dictionary

        :return: The resulting dictionary
        """
        if len(record) is len(self.__mapping_list):
            return {k: v for k,v in zip(self.__mapping_list, record)}
        else:
            raise ValueError("Mappings list must be same size as tuple")
