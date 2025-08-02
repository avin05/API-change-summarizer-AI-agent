# API Change Summarizer AI Agent

This project monitors changes in API documentation and summarizes updates automatically.

## Features

- Fetches API documentation from a given URL
- Computes and compares content hashes to detect changes
- Stores previous versions for change tracking
- Uses BeautifulSoup for HTML parsing

## Requirements

- Python 3.7+
- `requests`
- `beautifulsoup4`

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Edit `changelog_monitor.py` to set your documentation URL and file paths.

Run the monitor:

```bash
python changelog_monitor.py
```

## Configuration

- Update the URL in the script to point to your API documentation.
- The script saves and loads previous versions from local files.

## Author

avin05
