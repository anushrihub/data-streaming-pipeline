import logging
from datetime import datetime

from cassandra.auth import PlainTextAuthenticator
from cassandra.cluster import Cluster
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col

def create_keyspace(session):
    # create keyspace here

def create_table(session):
    # create table here

def insert_data(session, kwargs):
    # insertion here

def create_spark_connection():
    # creating spark connection
    s_conn = None
    try:
        s_conn = SparkSession.builder \
            .appName('SparkDataStreaming')
            .config('spark.jars.packages', "com.datastax.spark:spark-cassandra-connector_2.13:3.41","org.apache.spark:spark.-sql-kafka-0-10_2.13:3.4.1")\
            .config('spark.cassandra.connection.host','localhost') \
            .getOrCreate()

        s_conn.sparkContext.setLogLevel("ERROR")
    except Exception as e:
        logging.error(f"Couldn't create the spark session due to exception {e}")
    
    return s_conn

def create_cassandra_connection():
    # reconnectig to the cassandra cluster
    session = None
    try:
        cluster = Cluster(['localhost'])

        cas_session = cluster.connect()

        return cas_session
    
    except Exception as e:
        logging.error(f"Could not create cassandra connection due to {e}")
        return None;

    

if __name__ == '__main__':
    spark_conn = create_spark_connection()

    if spark_conn is not None:
        session = create_cassandra_connection

        if session is None:
            # do nothing
            


