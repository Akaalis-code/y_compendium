REFERENCE = https://kafka.apache.org/documentation/

# Intro :

    Apache Kafka is an open-source distributed event streaming platform for high-performance 
    data pipelines, streaming analytics, data integration, and mission-critical applications

    APACHE KAFKA is like a "Nervous System" transfering information in between organs(any data generators or receivers)

    In the world of DATA BASES  -   we had attributes sorrounded around THINGS
                                    That is, "what is that thing" ,leaving less emphasis on the thing's 
                                    changing nature as time proceeds 
    In the world Today          -   We have attributes sourounded by EVENTS (Time based)
                                    That is "At a particular time what is that Thing" , Having more 
                                    EMPHASIS on the thing's changing nature as time proceeds
    
    Kafka has "EVENTS first" approach rather than "THINGs first"

    Previous to kafka there were "ACTIVE MQ" , "RABBIT MQ" , "IBM MQ" which were being use as messaging queue technologies

    KAFKA s Cloud solutions are as below :
        Azure Event Hubs
        Amazon MSK (Managed Streaming for Apache Kafka)
        Confluent is enterprise level solution built around KAFKA with some extra needed tools

    
# How does it work :

    Kafka is a distributed system consisting of servers and clients that communicate via a high-performance TCP network protocol


# TERMINOLOGY :

    TOPIC   -
        PARTITION   -
            SEGMENT -
                LOG/STREAM -
                    EVENT   - 
                        Header(optional)    -
                        Key                 -
                        Value               -
                        Timestamp           -
    
    COMPACTED TOPIC     - 

    BROKERS             -
    PRODUCERS           -
    CONSUMERS           -
    ZOOKEEPER / KRAFT   -

# FEATURES of KAFKA :

    PRODUCERS and CONSUMERS are agnostic to each other and their functioning is completely decoupled
    Ensures each event is processed only once 
    data fault-tolerant and highly-available through REPLICATION across servers (Subject to change)


# APIS of KAFKA :

    ADMIN API       - to manage and inspect topics, brokers, and other Kafka objects
    PRODUCER API    - to publish (write) a stream of events to one or more Kafka topics
    CONSUMER API    - to subscribe to (read) one or more topics 
    Streams API     - It provides tools to process EVENTs , like the operations you do in SQL and SPARK
    Connect API     - It makes integration with any existing EVENT PRODUCERS , by providing you 
                        Ready made connectors tailored to each technology may it be RDBMS , Structured streaming 
                        or any cloud services