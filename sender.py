import pika
import json
import os
import sys
from dotenv import load_dotenv

# Get the .env variables
load_dotenv()

try:
    # rabbitMQ connection
    with pika.BlockingConnection(pika.ConnectionParameters(os.getenv('RABBITMQ_HOST'))) as connection:

        # open channel 
        channel = connection.channel()

        queue_name = os.getenv('RABBITMQ_QUEUE_NAME')

        # creating/declaring a queue
        channel.queue_declare(queue=queue_name)

        file_path = os.getenv('JSON_FILE_PATH')

        # read the file
        with open(file_path, "r") as file:
            data = json.load(file)

        for json_data in data:
            # Publish a message in the queue
            channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(json_data))
            print(" [{}] Sent {}".format(queue_name, json_data))

        print("Done.")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)