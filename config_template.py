# Database Configuration Template
# Copy this file to config.py and fill in your actual database credentials

import os

# Database configuration - uses environment variables with defaults
DB_CONFIG = {
    "user": os.getenv("DB_USER", "your_username"),
    "password": os.getenv("DB_PASSWORD", "your_password"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "airbnb_db")
}

# File paths for dataset
DATA_DIR = "dataset"
LISTINGS_FILE = os.path.join(DATA_DIR, "listings.csv.gz")
CALENDAR_FILE = os.path.join(DATA_DIR, "calendar.csv.gz")
