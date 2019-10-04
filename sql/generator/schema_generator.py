"""
Schema Creator

@author Andrew Evans
"""

from sql.query import create_schema_query_generator


class SchemaGenerator:

    def __init__(self, conn, close_conn_on_finish=True):
        """
        Constructor

        :param conn:    The connection
        :param close_conn_on_finish:    Whether to close the connection on finish
        """
        self.__conn = conn
        self.__do_close_conn = close_conn_on_finish


    def close_conn(self):
        """
        Close the cursor
        """
        if self.__conn is not None and self.__do_close_conn:
            self.__conn.close
            self.__conn = None


    def __enter__(self):
        """
        Turn this object into a closeable
        :return: self as a closeable
        """
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the object and attached connection

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        """
        self.close_conn()


    def create_schema(self, schema):
        """
        Create a schema from a schema object

        :param schema:  The schema object
        """
        qry = create_schema_query_generator.generate_query(schema)
        with self.__conn.cursor() as cursor:
            cursor.execute(qry)
