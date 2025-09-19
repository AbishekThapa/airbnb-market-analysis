import pandas as pd
from sqlalchemy import create_engine
import logging
import time
import warnings

# Reads private database credentials from config.py
try:
    import config
    from config import DB_CONFIG, LISTINGS_FILE, CALENDAR_FILE
except ImportError:
    print("FATAL ERROR: Configuration file 'config.py' not found.")
    print("Please copy 'config_template.py' to 'config.py' and fill it out.")
    exit()

# SETUP SECTION

def setup_logging():
    """Initializes logging to show progress in the terminal and save it to a file."""
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("pipeline.log", mode='w'),
            logging.StreamHandler()
        ]
    )
    warnings.filterwarnings("ignore")

def create_db_engine(config):
    """Creates a connection engine to our PostgreSQL database."""
    try:
        connection_url = (
            f"postgresql+psycopg2://{config['user']}:{config['password']}@"
            f"{config['host']}:{config['port']}/{config['database']}"
        )
        engine = create_engine(connection_url)
        
        connection = engine.connect()
        connection.close()
        
        logging.info("Successfully connected to the PostgreSQL database.")
        return engine
    except Exception as e:
        logging.error(f"Failed to connect to the database: {e}")
        return None

# ETL PROCESS SECTION

def run_pipeline(db_engine):
    """Runs the full ETL pipeline for all Airbnb files."""
    
    # LISTINGS FILE ETL
    logging.info("--- Starting ETL for Listings data ---")
    
    # EXTRACT
    try:
        listings = pd.read_csv(LISTINGS_FILE, compression='gzip', low_memory=False)
        logging.info(f"Successfully EXTRACTED {len(listings)} rows from {LISTINGS_FILE}")
    except FileNotFoundError:
        logging.error(f"File not found: {LISTINGS_FILE}. Aborting listings ETL.")
        return

    # TRANSFORM
    logging.info("TRANSFORMING listings data...")
    
    # Clean price column
    if 'price' in listings.columns:
        listings['price'] = pd.to_numeric(listings['price'].replace({r'\$': '', ',': ''}, regex=True), errors='coerce')
        logging.info("Cleaned the 'price' column.")
    
    logging.info(f"Rows remaining after dropping null prices: {len(listings)}")

    # Handle Duplicates
    duplicate_count = listings.duplicated().sum()
    if duplicate_count > 0:
        logging.info(f"Found {duplicate_count} duplicate rows. Removing them.")
        listings.drop_duplicates(inplace=True)
    else:
        logging.info("No duplicate rows found.")
        
    logging.info(f"Rows remaining after dropping duplicates: {len(listings)}")

    # LOAD
    if len(listings) > 0:
        logging.info(f"LOADING {len(listings)} cleaned listings rows into PostgreSQL...")
        listings.to_sql('listings', db_engine, if_exists='replace', index=False)
        logging.info("Successfully LOADED listings data into the 'listings' table.")
    else:
        logging.warning("No data left in listings to load after cleaning. Check the logs.")

    
    # # CALENDAR FILE ETL
    logging.info("--- Starting ETL for Calendar data ---")
    
    # EXTRACT
    try:
        calendar = pd.read_csv(CALENDAR_FILE, compression='gzip')
        logging.info(f"Successfully EXTRACTED {len(calendar)} rows from {CALENDAR_FILE}")
    except FileNotFoundError:
        logging.error(f"File not found: {CALENDAR_FILE}. Aborting calendar ETL.")
        return

    # TRANSFORM
    logging.info("TRANSFORMING calendar data...")
    for col in ['price', 'adjusted_price']:
        if col in calendar.columns:
            calendar[col] = pd.to_numeric(calendar[col].replace({r'\$': '', ',': ''}, regex=True), errors='coerce')
            logging.info(f"Cleaned the '{col}' column.")

    calendar.drop_duplicates(inplace=True)
    logging.info(f"Rows remaining after dropping duplicates: {len(calendar)}")

    # LOAD
    if len(calendar) > 0:
        logging.info(f"LOADING {len(calendar)} cleaned calendar rows into PostgreSQL...")
        calendar.to_sql('calendar', db_engine, if_exists='replace', index=False)
        logging.info("Successfully LOADED calendar data into the 'calendar' table.")
    else:
        logging.warning("No data left in calendar to load after cleaning. Check the logs.")


# SCRIPT EXECUTION SECTION
if __name__ == "__main__":
    setup_logging()
    
    logging.info("====== Starting Airbnb Data Pipeline ======")
    script_start_time = time.time()
    
    db_engine = create_db_engine(DB_CONFIG)
    
    if db_engine:
        run_pipeline(db_engine)
    else:
        logging.critical("Aborting pipeline due to database connection failure.")
        
    script_end_time = time.time()
    total_seconds = script_end_time - script_start_time
    logging.info(f"====== Pipeline Finished in {total_seconds:.2f} seconds ======")