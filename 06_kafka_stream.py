# 06_kafka_stream.py
from kafka import KafkaConsumer

# Change 'localhost:9092' & 'test-topic' to your setup
consumer = KafkaConsumer(
    "test-topic",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="latest",
    enable_auto_commit=True,
    group_id="demo-group"
)

print("Listening for messages...")
for msg in consumer:
    print("Received:", msg.value.decode("utf-8"))
    # break  # uncomment if you want to stop after first message
