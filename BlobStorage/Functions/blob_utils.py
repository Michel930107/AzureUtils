# blob_utils.py
# -*- coding: utf-8 -*-

import signal
import sys
from azure.storage.blob import BlobServiceClient

exit_handler = 0

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    global exit_handler
    exit_handler = 1

def delete_old_blobs(connection_string, cutoff_date):
    signal.signal(signal.SIGINT, signal_handler)
        
    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            connection_string, api_version='2019-12-12')

        containers = blob_service_client.list_containers()

        for container in containers:
            container_name = container['name']
            container_client = blob_service_client.get_container_client(container_name)

            blobs = container_client.list_blobs()

            for blob in blobs:
                blob_client = container_client.get_blob_client(blob.name)
                blob_properties = blob_client.get_blob_properties()
                creation_time = blob_properties.creation_time

                if exit_handler == 1:
                    sys.exit(0)

                if creation_time < cutoff_date:
                    print(f"Deleting blob: '{blob.name}' in container: '{container_name}'")
                    blob_client.delete_blob()
                else:
                    print(f"Skipping blob: '{blob.name}', creation time is after cutoff date")

    except Exception as e:
        print("An error occurred during deletion:", e)