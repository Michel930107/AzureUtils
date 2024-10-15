
# AzureBlobTool

![AzureBlobTool Logo](icon/icon.jpeg)

## Overview

**AzureBlobTool** is a console-based application designed to delete old blobs from an Azure Blob Storage account. This utility helps manage and clean up your Azure Blob Storage by removing files older than a specified cutoff date.

The tool can be customized to perform dry runs, set cutoff dates, and more.

---

## Features

- **Azure Blob Cleanup**: Easily delete blobs older than a given date.
- **Connection String Validation**: Validate Azure Storage connection strings for safe operations.
- **Cross-Platform Support**: Works on Windows, macOS, and Linux.
- **Custom Signal Handling**: Gracefully handle user interruptions (Ctrl + C).

---

## Prerequisites

Before you start, ensure you have the following installed on your system:

- Python 3.x
- Azure Storage Blob SDK
- PyInstaller (if you want to build the executable yourself)

You can install the required packages using:

```bash
pip install azure-storage-blob
```

---

## Installation

To install the tool, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/Michel930107/Automations/tree/main/BlobStorage
   ```

2. Navigate to the project directory:
   ```bash
   cd BlobStorage
   ```

3. Install the package:
   ```bash
   pip install .
   ```

4. (Optional) Build the executable using PyInstaller:
   ```bash
   pyinstaller --onefile --icon=icon.jpeg main.py
   ```

---

## Usage

After installation, the tool can be run as follows:

1. Open a terminal.
2. Run the executable or script:
   ```bash
   python main.py
   ```

   Or if you built the executable:
   ```bash
   ./AzureBlobTool.exe
   ```

3. Follow the prompts to:
   - Enter your Azure Storage connection string.
   - Specify the cutoff date for deleting blobs.
   - Confirm deletion of blobs.

Example of entering the connection string:

```plaintext
Please enter your Azure Storage connection string.
Example:
DefaultEndpointsProtocol=https;AccountName=your_account_name;AccountKey=your_account_key;EndpointSuffix=core.windows.net
```

---

## Configuration

You can modify the following parameters inside the script:

- **Cutoff Date**: Set the `cutoff_date` to define the threshold for blob deletion.
- **Signal Handling**: Customize the signal handler in `signal_utils.py` to handle interruptions.

---

## Running in Development Mode

If you'd like to run the script for testing purposes, you can run the following command:

```bash
python main.py
```

You can also modify `blob_utils.py` to perform a **dry run** by commenting out the `blob_client.delete_blob()` line and observing the blobs that would be deleted:

```python
# Dry run mode
# blob_client.delete_blob()  # Comment this line for a dry run.
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

---

## Author

- **Michel Borrego**
  - Email: michel@fxstreet.com, michelbh93@gmail.com
  - GitHub: [Michel930107](https://github.com/Michel930107/Automations/tree/main/BlobStorage)

---

## Acknowledgments

- This tool uses the Azure Storage Blob SDK for Python.
- Special thanks to contributors and the open-source community for their support.

---

Feel free to contribute to the project or submit issues via GitHub.

---