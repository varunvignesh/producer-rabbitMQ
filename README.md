# RabbitMQ Producer App

## Requirements

- Python 3.8.x

## Setup

1. Clone the repository

2. Create a virtual environment

   ```
   python3.8 -m venv ./venv
   ```

3. Activate the virtual environment

   ```
   source venv/bin/activate
   ```

4. Install the requirements

   ```
   pip install -r requirements.txt
   ```

5. Create a .env file and add the following variables from .env.example

6. To send the data to the Queue

   ```
   python sender.py
   ```

## Note

I have update the json file to be in an array _(assuming that was left out?)_
