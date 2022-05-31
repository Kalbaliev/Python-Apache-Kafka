
# Apache Kafka on Python 

First of All, for using **Apache Kafka** on Python we have to up Kafka, Zookeeper Servers on Docker.
Because Kafka depends on Apache Zookeeper




## Apache Zookeeper, Kafka up on Docker

Pull __Zookeeper, Kafka__ image from [DockerHub](https://hub.docker.com/search?q=zookeeper)
```console
docker pull zookeeper

docker pull confluentinc/cp-kafka
```
Apache Zookeeper port is 2181, Apache Kafka port is 9092.

`docker-compose.yml` file which help you  to up two servers with dependencies

**But there is an important point here, you have to change ip address with your own ip**
![IpAddress](https://i.ibb.co/4PcpLbP/ipconfig.png)

```console
docker-compose up
```




# Python Coding
```python
  pip install kafka-python
```
## Import Classes from kafka on Python
```python

from kafka import KafkaProducer,KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic

```
## Pub-Sub and Queue Models with `python-kafka.py` file

There is 6 methods which help us to use Kafka for Pub/Sub and Queue Models
- Create
- Delete
- Produce
- Consume
- Show Topics
- Show Partition Size

#### Create New Topic with partitions
- ***`createTopic(topic_name,partition_size=1)`*** - give topic's name and parition size (optional)
```console
  python python-kafka.py createTopic "first-topic" 2
```
#### Delete Topic(s)
- ***`deleteTopics(topic_names)`*** - give topics' names from list type
```console
  python python-kafka.py deleteTopics ['first-topic']
```


#### Produce Message to Topic 
- ***`produceMessage(topic_name,msg,partition=0)`*** - give topic's name, message and parition's location (optional)
```console
  python python-kafka.py produceMessage 'first-topic' 'Hello From Producer' 0
```
#### Consume Message from Topic 
- ***`consumeMessage(topic_name,group_id)`*** - give topic's name and group_id

Thanks to `group_id` we can use Apache Kafka both Pub/Sub and Queue Models
- Queue - Consumers in same group_id and topic
- Pub/Sub - Consumers in same topic but different group_ids

```console
  python python-kafka.py consumeMessage 'first-topic' 'group-1'
```

#### Show Topics
- ***`showTopics()`*** 
```console
  python python-kafka.py showTopics
```
#### Show Topic's partition size
- ***`showPartitions(topic_name)`*** - give topic's name
```console
  python python-kafka.py showPartitions 'first-topic'
```


