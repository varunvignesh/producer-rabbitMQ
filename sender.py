import pika
import json
import os
import sys
import logging
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.INFO)

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
            logging.info(" [{}] Sent {}".format(queue_name, json_data))

        logging.info("Done.")

except Exception as e:
    logging.error("Error: {}".format(e))
    sys.exit(1)