# main.py
# -*- coding: utf-8 -*-

import os
from datetime import datetime, timezone
from blob_utils import delete_old_blobs

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_connection_string(connection_string):
    if not connection_string.strip():
        print("\n[ERROR] Connection string cannot be empty.\n")
        return False

    required_keys = ['DefaultEndpointsProtocol', 'AccountName', 'AccountKey', 'EndpointSuffix']
    
    parts = connection_string.split(';')
    connection_dict = {}

    for part in parts:
        if '=' in part:
            key, value = part.split('=', 1)
            connection_dict[key] = value.strip()
    
    missing_keys = [key for key in required_keys if key not in connection_dict]
    if missing_keys:
        print(f"\n[ERROR] The connection string is missing the following required keys: {', '.join(missing_keys)}\n")
        return False

    if not connection_dict.get('AccountKey'):
        print("\n[ERROR] 'AccountKey' cannot be empty.\n")
        return False

    print("\n[SUCCESS] Connection string is valid.\n")
    return True

def get_valid_connection_string():
    while True:
        print("Please enter your Azure Storage connection string.")
        print("Example:")
        print("DefaultEndpointsProtocol=https;AccountName=your_account_name;AccountKey=your_account_key;EndpointSuffix=core.windows.net")
        connection_string = input("\nConnectionString: ")

        if validate_connection_string(connection_string):
            return connection_string
        print("[INFO] Please try again.")
        input("\nPress Enter to retry...")  
        clear_console() 

def get_valid_cutoff_date():
    date_format = "%Y-%m-%d"
    while True:

        cutoff_date_input = input(f"\nPlease enter the cutoff date in format '{date_format}' (e.g., '2020-01-01'): ")
        try:
            cutoff_date = datetime.strptime(cutoff_date_input, date_format).replace(tzinfo=timezone.utc)
            return cutoff_date
        except ValueError:
            print(f"\n[ERROR] Invalid date format. Please enter the date in the format '{date_format}'.")
            print("[INFO] Please try again.")
            input("\nPress Enter to retry...")
            clear_console()


def main():
    connection_string = get_valid_connection_string()

    # Get a valid cutoff date
    cutoff_date = get_valid_cutoff_date()
    
    # Confirm with the user before proceeding
    confirm = input(f"\nAre you sure you want to delete all blobs created before {cutoff_date.isoformat()}? Type 'yes' to confirm: ")
    if confirm.lower() == 'yes':
        delete_old_blobs(connection_string, cutoff_date)
        print("\n[SUCCESS] Deletion completed.\n")
    else:
        print("\n[INFO] Deletion canceled.\n")

if __name__ == "__main__":
    main()