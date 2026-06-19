from kafka import KafkaConsumer
import json

print("=== Medium Fraud Alert System ===")

user_id_input = input("Enter your userId: ")

try:
    user_id = int(user_id_input)
except ValueError:
    print("Invalid User ID")
    exit()

consumer = KafkaConsumer(
    'medium-fraud-notification',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print(f"Logged in as User {user_id}")
print("Listening for Medium Fraud Alerts...")

for message in consumer:
    data = message.value

    # Show only alerts for this user
    if data.get("userId") == user_id:

        print("\nMEDIUM FRAUD ALERT")
        print(f"Transaction ID : {data.get('tx_id')}")
        print(f"User ID        : {data.get('userId')}")
        print(f"Amount         : {data.get('amount')}")
        print(f"Timestamp      : {data.get('timestamp')}")
        print("-" * 40)