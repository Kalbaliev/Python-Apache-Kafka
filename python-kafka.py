from kafka import KafkaProducer,KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic

import sys,ast


kafka_server = ['localhost:9092']
admin_client = KafkaAdminClient(bootstrap_servers=kafka_server)


### Create and Delete Topics with partitions
def createTopic(topic_name,partition_size=1):

    existing_topic_list = admin_client.list_topics()
    if topic_name not in existing_topic_list:
        print('Topic : {} added '.format(topic_name))
        topic_list=[NewTopic(name=topic_name, num_partitions=int(partition_size), replication_factor=1)]
        try:
            admin_client.create_topics(new_topics=topic_list, validate_only=False)
            print("Topic Created Successfully")
        except  Exception as e:
            print(e)
    else:
        print('Topic : {} already exist'.format(topic_name))

def deleteTopics(topic_names):
    try:
        admin_client.delete_topics(topics=topic_names)
        print("Topic(s) Deleted Successfully")
    except  Exception as e:
        print(e)

def produceMessage(topic_name,msg,partition=0):
    producer = KafkaProducer(bootstrap_servers=kafka_server)
    producer.send(topic_name, bytes(msg,'utf-8'),partition=int(partition)) # convert to byte b'message' or bytes('message','utf-8')
    producer.flush()

def consumeMessage(topic_name,group_id):
    consumer = KafkaConsumer(topic_name,
                            group_id=group_id,
                            auto_offset_reset='earliest', 
                            enable_auto_commit=True,
                            bootstrap_servers=kafka_server)
    consumer.subscribe(topic_name)
    for message in consumer:
        print (f"Topic: {message.topic} --- Partition: {message.partition} --- OffSet: {message.offset}\nKey: {message.key} --- Value: {message.value.decode('utf-8')}")
        
def showTopics():
    print("Topics' List: ",admin_client.list_topics())

def showPartitions(topic_name):
    consumer = KafkaConsumer(topic_name,bootstrap_servers=kafka_server)
    print("Partition's Size: ",len(consumer.partitions_for_topic(topic_name)))
    sys.exit()
if __name__ == "__main__":
    args = sys.argv
    
    if args[1]=='produceMessage':
        print("Message Sent")
        if len(args)==4:
            globals()[args[1]](args[2],args[3])
        else:
            globals()[args[1]](args[2],args[3],args[4])
    elif args[1]=='consumeMessage':
        globals()[args[1]](args[2],args[3])
    elif args[1]=='createTopic':
        if len(args)==4:
            globals()[args[1]](args[2],args[3])
        else:
            globals()[args[1]](args[2])
    elif args[1]=='deleteTopics':
        args[2]=bytes(args[2],"utf-8")
        args[2] = args[2].decode("UTF-8")
        args[2]= ast.literal_eval(args[2])
        globals()[args[1]](args[2])
    elif args[1]=='showTopics':
        globals()[args[1]]()
    elif args[1]=='showPartitions':
        globals()[args[1]](args[2])