"""
Postgres Record iterator

@author Andrew Evans
"""
from psycopg2.extras import RealDictCursor

from sql.record_to_dict import RecordToDict


class PGRecordIterator:
    """
    Generates blocks of records from streams via psycopg2.
    """

    def __init__(self,
                 conn,
                 query,
                 name=None,
                 itersize=2000,
                 cursor_factory=RealDictCursor):
        """
        Constructor

        :param conn:    Postgres connection
        :param query:   Query to use
        :param name:    Name for the cursor
        :param itersize:    Max number of records to iterate through
        """
        self.__conn = conn
        self.__query = query
        self.__name = name
        self.__cursor = None
        self.__itersize = itersize
        self.__cursor_factory = cursor_factory

    def set_cursor_name(self, name):
        """
        Set the cursor name
        """
        self.__name = name

    def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Close any open cursor if open

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        """
        if self.__cursor:
            self.close_cursor()

    def close_cursor(self):
        """
        Check and close the cursor as required
        """
        if self.__cursor:
            self.__cursor.close()
            self.__cursor = None

    def __enter__(self):
        """
        Make closeable
        :return: closeable self
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close cursor if open
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self.close_cursor()

    def __iter__(self):
        """
        Creates an iterator from the query
        :return:    This class as an initiated iterator
        """
        if self.__query:
            if self.__name and not self.__cursor:
                self.__cursor = self.__conn.cursor(
                    self.__name, cursor_factory=self.__cursor_factory)
                self.__cursor.itersize = self.__itersize
            elif not self.__cursor:
                self.__cursor = self.__conn.cursor()
            self.__cursor.execute(self.__query)
        else:
            raise ValueError("PG Query for Record Iterator Cannot Be Null")
        return self

    def __next__(self):
        """
        Get the next value in the iterator
        :return:    The next tuple
        """
        rdict = self.__cursor.fetchone()
        if rdict is not None:
            return dict(rdict)
        else:
            raise StopIteration