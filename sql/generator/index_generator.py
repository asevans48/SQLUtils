"""
Generate indices

@author Andrew Evans
"""


class IndexGenerator:
    """
    Index generator class
    """

    def __init__(self, conn):
        """
        Constructor

        :param conn:    The connection
        """
        self.__conn = conn

    def close_conn(self):
        """
        Close the connection
        """
        if self.__conn:
            self.__conn.close()

    def __enter__(self):
        """
        Turn this class into a closeable
        :return: This object as a closeable
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the connection if open

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self.close_conn()

    def create_indices(self, indices):
        """
        Create the actual indices

        :param indices: The indices to create
        """
        if indices:
            for index in indices:
                pass


