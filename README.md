
# Realtime Data Streaming Pipeline
## Introduction
Built an end-to-end data engineering pipeline that implements the complete data lifecycle, from ingestion and processing to storage. Leveraged Apache Kafka and Zookeeper for real-time event streaming, Apache Spark for distributed data processing, Apache Airflow for workflow orchestration, PostgreSQL as a staging database, and Cassandra for scalable storage. Containerized the entire stack using Docker for reproducible deployment and simplified local development.


## System Architecture

```text
+------------------+     +------------------+     +------------------+     +-------------------+     +------------------+
|  Random User API | --> |  Apache Airflow  | --> |    PostgreSQL    | --> |       Kafka       | --> |   Spark Cluster  |
+------------------+     +------------------+     +------------------+     +---------+---------+     +---------+--------+
                                                                                         |                         |
                                                                                         |                         |
                                         +-------------------------+----------------------+                        |
                                         |                         |                                               |
                                         v                         v                                               |
                                  +--------------+        +------------------+                                     |
                                  |  Zookeeper   |        | Control Center   |                                     |
                                  +--------------+        +------------------+                                     |
                                                                                                                   |
                                                           +----------------+                                      |
                                                           | Schema Registry|                                      |
                                                           +----------------+                                      |
                                                                                                                   |
                                                                                                                   v
                                                                                                         +------------------+
                                                                                                         |   Spark Master   |
                                                                                                         +---------+--------+
                                                                                                                   |
                                                                                         +-------------------------+-------------------------+
                                                                                         |                         |                         |
                                                                                         v                         v                         v
                                                                                  +-------------+          +-------------+          +-------------+
                                                                                  |SparkWorker  |          |SparkWorker  |          |SparkWorker  |
                                                                                  +------+------+          +------+------+          +------+------+
                                                                                         \                         |                         /
                                                                                          \________________________|________________________/
                                                                                                                   |
                                                                                                                   v
                                                                                                         +------------------+
                                                                                                         |    Cassandra     |
                                                                                                         +------------------+

                                          (All services run in Docker containers)
```
```



- **Data Source**: Generates sample user records.
- **Apache Airflow**: Orchestrates the ETL workflow and loads data into PostgreSQL.
- **PostgreSQL**: Stores raw ingested data before streaming.
- **Apache Kafka and Zookeeper**: Used for streaming data from PostgreSQL to the processing engine.
- **Control Center and Schema Registry**: Helps in monitoring Kafka topics and manages schemas.
- **Apache Spark**: For data processing with its master and worker nodes.
- **Cassandra**: Where the processed data will be stored.


## Technologies Used
- Python
- Apache Airflow
- PostgreSQL
- Apache Kafka
- Apache Zookeeper
- Apache Spark
- Cassandra
- Docker
