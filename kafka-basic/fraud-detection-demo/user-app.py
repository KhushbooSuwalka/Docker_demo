from kafka import KafkaConsumer
import json

def user_login_and_listen():
    print("=== Fraud Alert System ===")
    user_id_input = input("Enter your userId to login: ")

    try:
        user_id = int(user_id_input)
    except ValueError:
        print("Invalid ID. Exiting.")
        return

    print(f"Logged in as User {user_id}. Listening for alerts...")

    # Listen to kafka:9092
    consumer = KafkaConsumer(
        'fraud-notification',
        bootstrap_servers=['kafka:9092'],
        auto_offset_reset='latest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        alert_data = message.value

        # Check if alert belongs to logged-in user
        if alert_data.get("userId") == user_id:
            print("\n FRAUD ALERT RECEIVED!")
            print(f"Transaction ID : {alert_data.get('tx_id')}")
            print(f"Amount         : {alert_data.get('amount')}")
            print(f"User ID        : {alert_data.get('userId')}")
            print(f"Timestamp      : {alert_data.get('timestamp')}")
            print("-" * 40)

if __name__ == "__main__":
    user_login_and_listen()