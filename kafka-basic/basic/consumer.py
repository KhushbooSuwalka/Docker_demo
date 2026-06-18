from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "demo-topic",
    bootstrap_servers="kafka:9092",
    auto_offset_reset="earliest",
    value_deserializer = lambda x: json.loads(x.decode("utf-8"))
)
# auto_offset_reset = "earliest" means the consumer will read the early messages also
# value_deserializer :- This decodes bytes into Python objects (which are in dictionary format) 
# json.loads(...) :- converts json string to dictionary
# x.decode("utf-8") :- Converts bytes to json string. 

for msg in consumer:
    print(msg.value)