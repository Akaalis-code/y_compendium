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

    KAFKA s various tools and solutions :
        Azure Event Hubs .
        Amazon MSK (Managed Streaming for Apache Kafka) .
        Confluent is enterprise level solution built around KAFKA with some extra needed tools .
        QUIX STREAMS gives python library for using KAFKA STREAMS I think (Subject to change) .

    KAFKA was Developed by LINKEDIN around 2011 using SCALA and JAVA , Right now it is being maintained by APACHE 

# Eagle s eye VIEW of things involved in KAFKA :
    Producers : the systems who produce data continuously
    Brokers   : These are (KAFKA clusters + ZOOKEEPER)  which sit between PRODUCERS and CONSUMERS 
    Consumers : The systems which are supposed to receive that data 

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

    BROKERS             - These are servers which mediate communication between two different systems 
    MESSEGES            - These can be info in the format of BYTE ARRAYS , JSON , AVRO , STRInG 
    CLUSTERS            - A set of servers which are acting as KAFKA brokers 
    PRODUCERS           -
    CONSUMERS           -
    CONSUMER GROUP      -
    ZOOKEEPER           - 1) It helps co-ordinate the MULTI NODE BROKER CLUSTER setup , in terms of electing the leader and other functions
                          2) It keeps track of number of CLUSTERS and PARTITIONS and notify that info to PRODUCERS and CONSUMERS
                          3) Message OFFSET is maintained by zookeeper (Subject to correction) 
    KRAFT               -
    OFFSET              -

# FEATURES of KAFKA :

    PRODUCERS and CONSUMERS are agnostic to each other and their functioning is completely decoupled .
    Ensures each event is processed only once .
    Data fault-tolerant and highly-available through REPLICATION across servers (Subject to change) .
    ASYNCHRONOUS communication - The producers dont have to wait to make sure consumers are properly consuming ,that is KAFKA s job (subject to correction)


# APIS of KAFKA :

    ADMIN API       - to manage and inspect topics, brokers, and other Kafka objects
    PRODUCER API    - to publish (write) a stream of events to one or more Kafka topics
    CONSUMER API    - to subscribe to (read) one or more topics 
    Streams API     - It provides tools to process EVENTs , like the operations you do in SQL and SPARK
    Connect API     - It makes integration with any existing EVENT PRODUCERS , by providing you 
                        Ready made connectors tailored to each technology may it be RDBMS , Structured streaming 
                        or any cloud services



# KAFKA CLUSTER SETUP :

    Kafka can work in -

        Single node setup :
            Single node single broker -
            Single node multi broker  -

        Multi node setup:
            Multi node Multi broker -