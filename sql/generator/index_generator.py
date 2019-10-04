"""
Generate indices

@author Andrew Evans
"""

from sql.query import index_query_generator


class IndexGenerator:
    """
    Index generator class
    """

    def __init__(self, conn, close_conn_on_finish=True):
        """
        Constructor

        :param conn:    The connection
        :param close_conn_on_finish: close connetion on exit
        """
        self.__conn = conn
        self.__do_close_conn = close_conn_on_finish

    def close_conn(self):
        """
        Close the connection
        """
        if self.__conn and self.__do_close_conn:
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
                q = index_query_generator.generate_index_query(index)
                with self.__conn.cursor() as cursor:
                    cursor.execute(q)
