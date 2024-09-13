import json
import requests
from faker import Faker
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta
import random

fake = Faker()

OPENSEARCH_URL = 'http://localhost:9200'
INDEX_NAME = 'fake-data2-index'
USERNAME = 'admin'
PASSWORD = 'Omnivista@123'

headers = {
    "Content-Type": "application/json"
}

def create_index():
    index_settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "name": {"type": "text"},
                "address": {"type": "text"},
                "email": {"type": "keyword"},
                "date_of_birth": {"type": "date"},
                "phone_number": {"type": "keyword"},
                "job": {"type": "text"},
                "@timestamp": {"type": "date"}
            }
        }
    }

    response = requests.put(
        f"{OPENSEARCH_URL}/{INDEX_NAME}",
        headers=headers,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        data=json.dumps(index_settings)
    )
    print(f"Create index reponse: {response.status_code}, {response.text}")

def generate_random_timestamp():
    start_time = datetime.now() - timedelta(days=5)
    end_time = datetime.now() - timedelta(days=3)
    random_time = start_time + (end_time - start_time) * random.random()
    return random_time.isoformat()

def generate_and_index_data(num_records):
    for _ in range(num_records):
        # Generate fake data with a random timestamp
        doc = {
            "name": fake.name(),
            "address": fake.address(),
            "email": fake.email(),
            "date_of_birth": fake.date_of_birth().strftime('%Y-%m-%d'),
            "phone_number": fake.phone_number(),
            "job": fake.job(),
            "@timestamp": generate_random_timestamp()
        }

        # Index the data to OpenSearch
        response = requests.post(
            f"{OPENSEARCH_URL}/{INDEX_NAME}/_doc",
            headers=headers,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),  # Add Basic Authentication
            data=json.dumps(doc)
        )
        if response.status_code == 201:
            print(f"Successfully indexed: {doc['name']}, @timestamp: {doc['@timestamp']}")
        else:
            print(f"Failed to index document: {response.status_code}, {response.text}")

if __name__ == "__main__":
    # Create index in OpenSearch
    create_index()

    # Generate and index fake data
    generate_and_index_data(100)  # Change the number as needed
