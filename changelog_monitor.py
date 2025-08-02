import hashlib
import os
import requests
from bs4 import BeautifulSoup

def fetch_doc(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching documentation: {e}")
        return ""

def compute_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def load_last(path):
    if not os.path.exists(path):
        return ""
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        print(f"Error loading last version: {e}")
        return ""

def save_current(content, path):
    try:
        with open(path, "w") as f:
            f.write(content)
    except Exception as e:
        print(f"Error saving current version: {e}")